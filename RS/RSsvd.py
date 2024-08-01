from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import numpy as np
import pandas as pd
header = ['user_id', 'item_id', 'rating', 'timestamp']
src_data = pd.read_csv('../ml-100k/u.data', sep='\t', names=header)
src_data.head()

n_users = src_data.user_id.nunique()                   # 用户、物品数去重统计
n_items = src_data.item_id.nunique()

from sklearn.model_selection import train_test_split  # 训练集、测试集拆分
train_data, test_data = train_test_split(src_data, test_size=0.3)

train_data_matrix = np.zeros((n_users, n_items))      # 训练集 用户-物品矩阵
for line in train_data.itertuples():
    train_data_matrix[line[1]-1, line[2]-1] = line[3]

test_data_matrix = np.zeros((n_users, n_items))       # 测试集 用户-物品矩阵
for line in test_data.itertuples():
    test_data_matrix[line[1]-1, line[2]-1] = line[3]

import scipy.sparse as sp
from scipy.sparse.linalg import svds

u, s, vt = svds(train_data_matrix, k = 20)     #获取奇异值分解因子。选择K.
s_diag_matrix=np.diag(s)
svd_prediction = np.dot(np.dot(u, s_diag_matrix), vt)

u.shape                                        #数据感知
s.shape
vt.shape
s_diag_matrix.shape
svd_prediction.shape

#np.cumsum([1,2,3,4,5,6])->array([ 1,  3,  6, 10, 15, 21], dtype=int32)
k=942
u, s, vt = svds(train_data_matrix, k)
scumrate = pd.DataFrame({'cumsum':np.cumsum(s[::-1])/np.sum(s)})
# 查看预测矩阵值分布
print("预测矩阵值分布:")
print(pd.Series(np.percentile(svd_prediction, np\
                        .arange(0, 101, 10)))\
                        .map("{:.2f}".format))
# 查看训练数据矩阵值分布
print("训练数据矩阵值分布:")
print(pd.Series(np.percentile( train_data_matrix, np\
                        .arange(0, 101, 10)))\
                        .map("{:.2f}".format))

# 查看训练数据矩阵非0值分布
pd.Series(np.percentile( train_data_matrix[train_data_matrix.nonzero()],
                        np.arange(0, 101, 10))).map("{:.2f}".format)

svd_prediction[svd_prediction<0] = 0       # 将预测值中小于0的值，赋值为0
svd_prediction[svd_prediction>5] = 5       # 将预测值中大于5的值，赋值为5
print("svd_prediction:{}".format(svd_prediction))

# 训练集预测------只取预测数据集中有评分的数据集，进行评估
from sklearn.metrics import mean_squared_error
from math import sqrt
prediction_flatten = svd_prediction[train_data_matrix.nonzero()]

train_data_matrix_flatten = train_data_matrix[train_data_matrix.nonzero()]

train_SVD_mean_squared_error=sqrt(mean_squared_error(prediction_flatten, train_data_matrix_flatten))

# 测试集预测------只取预测数据集中有评分的数据集
from sklearn.metrics import mean_squared_error
from math import sqrt
prediction_flatten = svd_prediction[test_data_matrix.nonzero()]
print("预测：{}".format(prediction_flatten[:5]))
test_data_matrix_flatten = test_data_matrix[test_data_matrix.nonzero()]

test_SVD_mean_squared_error=sqrt(mean_squared_error(prediction_flatten, test_data_matrix_flatten))

print("Train:SVD_mean_squared_error:{}".format(train_SVD_mean_squared_error))
print("Test:SVD_mean_squared_error:{}".format(test_SVD_mean_squared_error))

## 实际推荐过程中，需要在预测集中过滤掉已经评级过的物品
svd_p_df = pd.DataFrame(svd_prediction)
svd_p_df = svd_p_df[pd.DataFrame(train_data_matrix) == 0]  # 只选择在训练集没有被评过分的部分# 利用分位数函数获取每个用户的得分最高的topk个物品
topk = 10                                    # 看top10的相似
quantile = 1-topk/float(svd_p_df.shape[1])  # topk的分位数
# 预测矩阵的topk 0,1矩阵   每行(每个用户)的topk分位数值
# 如果topk分位数值为0,则意味此行大于0的列数<topk个，则为了后面的处理需要取一个比0稍微大一点点的值
topk_threshold = svd_p_df.quantile(q=quantile, axis=1).map(lambda x: max(x, 0.00000000000001))
# 对每行中前topk的数值标记为1，否则标记为0
svd_p_topk = svd_p_df.sub(topk_threshold, axis=0).applymap(lambda x:1 if x>=0 else 0)
## 测试矩阵的topk 0,1矩阵
test_data_m_df = pd.DataFrame(test_data_matrix)
# 每行(每个用户)的topk分位数值
# 如果topk分位数值为0,则意味此行大于0的列数<topk个，则为了后面的处理需要取一个比0稍微大一点点的值
topk_threshold = test_data_m_df.quantile(q=quantile, axis=1).map(lambda x: max(x, 0.000000001))
# 对每行中前topk的数值标记为1，否则标记为0
test_data_m_topk = test_data_m_df.sub(topk_threshold, axis=0).applymap(lambda x:1 if x>=0 else 0)
# 并集矩阵
inter_m = test_data_m_topk*svd_p_topk
print("inter_m:")
print(inter_m)
# Jaccard相似性
Jaccard = inter_m.sum().sum() / np.double(test_data_m_topk.sum().sum() + svd_p_topk.sum().sum() - inter_m.sum().sum())
print("相似度：{}".format(Jaccard))
# 准确率计算
Accuracy= inter_m.sum().sum() / np.double(svd_p_topk.sum().sum())
print("准确率：{}".format(Accuracy))
# 召唤率计算
recall=inter_m.sum().sum() / np.double(test_data_m_topk.sum().sum())
print("召唤率：{}".format(recall))