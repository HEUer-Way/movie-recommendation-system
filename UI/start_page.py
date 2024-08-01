from functools import partial

from PyQt5.QtWidgets import QApplication, QMainWindow
from pylab import *

import GlobalFun
import RS.RSitemcf
import RS.RSsklearnSVD
import RS.RSusercf
import recommendation_system_page as mypage
from RS.deep_learning_recommend.recommend import Recommend


def start_recommend(ui):
    user_id = ui.lineEdit_3.text()
    if user_id == '':
        # ui.label_27.setText('')
        ui.tip1()
    else:
        movies = ''
        conn, cur = GlobalFun.ConnectSql()
        cur.execute(
            'select distinct title from movierecommender.movies , movierecommender.ratings where userid = {} and ratings.movieId = movies.movieId'.format(user_id))
        data = cur.fetchall()
        count = 20
        for res in data:
            if (count != 0) :
                movies += res[0] + '\n'
                count -= 1

        GlobalFun.Closesql(conn, cur)
        ui.label_27.setText(str(movies))



        if ui.comboBox_2.currentText() == '基于深度学习ALS推荐算法':
            movies = ''
            conn, cur = GlobalFun.ConnectSql()
            r = Recommend()
            res_arr = r.recommend(int(user_id), 10)
            for res in res_arr:
                cur.execute(
                    'select distinct title from movierecommender.movies where movieid = {}'.format(int(res[1])))
                data = cur.fetchall()
                # 拿到离线用户推荐信息
                if len(data) != 0:
                    movies += data[0][0] + '\n'

            GlobalFun.Closesql(conn, cur)
            ui.label_28.setText(str(movies))

        elif ui.comboBox_2.currentText() == '基于SVD推荐算法':
            dataFile = '../ml-100k/u.data'
            df, n_users, n_items, train_data, test_data = RS.RSsklearnSVD.splitData(
                dataFile, test_size=0.25)
            # 计算相似度
            train_data_matrix, test_data_matrix, user_similarity, item_similarity, item_popular = RS.RSsklearnSVD.calc_similarity(
                n_users, n_items, train_data, test_data)
            # 基于模型的协同过滤
            # ...
            # 计算MovieLens数据集的稀疏度 （n_users，n_items 是常量，所以，用户行为数据越少，意味着信息量少；越稀疏，优化的空间也越大）
            # 计算稀疏矩阵的最大k个奇异值/向量
            u, s, vt = RS.RSsklearnSVD.svds(train_data_matrix, k=15)
            s_diag_matrix = np.diag(s)
            svd_prediction = np.dot(np.dot(u, s_diag_matrix), vt)
            # 推荐结guo
            movies = ''
            conn, cur = GlobalFun.ConnectSql()
            res_arr = RS.RSsklearnSVD.recommend(int(user_id), svd_prediction, train_data_matrix, test_data_matrix)
            for res in res_arr:
                cur.execute(
                    'select distinct title from movierecommender.movies where movieid = {}'.format(res))
                data = cur.fetchall()
                # 拿到离线用户推荐信息
                if len(data) != 0:
                    movies += data[0][0] + '\n'

            GlobalFun.Closesql(conn, cur)
            ui.label_28.setText(str(movies))

        elif ui.comboBox_2.currentText() == '基于用户的推荐算法':
            ratingfile = '../ml-100k/u.data'
            # 创建UserCF对象
            usercf = RS.RSusercf.UserBasedCF()
            # 将数据按照 7:3的比例，拆分成：训练集和测试集，存储在usercf的trainset和testset中
            usercf.generate_dataset(ratingfile, pivot=0.7)
            # 计算用户之间的相似度
            usercf.calc_user_sim()
            # 查看推荐结果用户
            movies = ''
            ids = []
            print(usercf.recommend(str(user_id)))
            conn, cur = GlobalFun.ConnectSql()
            res_arr = usercf.recommend(str(user_id))
            for res in res_arr:
                ids.append(res[0])
                cur.execute(
                    'select distinct title from movierecommender.movies where movieid = {}'.format(res[0]))
                data = cur.fetchall()
                # 拿到离线用户推荐信息
                if len(data) != 0:
                    movies += data[0][0] + '\n'

            GlobalFun.Closesql(conn, cur)
            ui.label_28.setText(str(movies))

        elif ui.comboBox_2.currentText() == '基于项目的推荐算法':
            ratingfile = '../ml-100k/u.data'
            # 创建ItemCF对象
            itemcf = RS.RSitemcf.ItemBasedCF()
            # 将数据按照 7:3的比例，拆分成：训练集和测试集，存储在usercf的trainset和testset中
            itemcf.generate_dataset(ratingfile, pivot=0.7)
            # 计算用户之间的相似度
            itemcf.calc_movie_sim()
            # 查看推荐结果用户
            movies = ''
            ids = []
            conn, cur = GlobalFun.ConnectSql()
            res_arr = itemcf.recommend(str(user_id))
            for res in res_arr:
                ids.append(res[0])
                cur.execute(
                    'select distinct  title from movierecommender.movies where movieid = {}'.format(res[0]))
                data = cur.fetchall()
                # 拿到离线用户推荐信息
                if len(data) != 0:
                    movies += data[0][0] + '\n'
            GlobalFun.Closesql(conn, cur)
            ui.label_28.setText(str(movies))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = mypage.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 推荐按钮
    ui.pushButton_5.clicked.connect(partial(start_recommend, ui))
    sys.exit(app.exec_())
