早期的电影推荐系统只需获取简单的用户信息，随着推荐系统发展，电影推荐系统由简单的
信息获取转变为和用户交互的系统，需要考虑用户多兴趣和用户兴趣转变的情况，将数据挖掘应
用到用户信息获取中，挖掘用户的隐性需求。要实现被顾客接受和认可的个性化推荐，设计准确、
高效率的个性化推荐算法是核心需求。当然，不同的推荐算法各有优缺点。为了克服各自的缺点，
可以将各种推荐方法混合使用，以提高推荐精度和覆盖率。同时，大数据技术和主流的人工智能
技术等相关领域的引入扩宽了推荐算法的思路。要使推荐系统为广大用户所接受，要对推荐系统
作出客观综合的评价，其中，推荐结果的准确性和可信性是非常重要的两个方面。
1. 大数据模块设计：使用 Scala 语言，采用 Hadoop+Spark 统一部署实验环境，基于模型的推
荐算法，使用 IDEA 编译运行 Scala 语言实现 ALS 算法，并打包生成应用 JAR 包，最后部署到
Spark。
2. 算法模块：使用 python 语言，将实现后的推荐算法（基于深度学习 ALS 推荐，基于 SVD 推
荐算法，基于项目推荐，基于用户推荐）集成于系统中，供用户选择。用户可在系统中查看已观
看的电影，并且根 据可选推荐算法，对其进行电影推荐。输入用户 id，再根据下拉框选择相应
的推荐算法，最后点击 “推荐”即可完成电影推荐。
3. 数据表设计：数据库的数据表主要包括用户信息表、电影信息表、用户评分表，电影标签表。
用以界面存储展示数据
4. UI 设计：采用 PyQT 用以创建简易应用程序。它是 Python 编程语言和 Qt 库的融合。
效果展示，左侧展示用户观影记录，右侧为推荐电影
初始界面展示：
![image](https://github.com/HEUer-Way/movie-recommendation-system/blob/master/UI/image/%E5%88%9D%E5%A7%8B%E7%95%8C%E9%9D%A2.jpg)
![image](https://github.com/HEUer-Way/movie-recommendation-system/blob/master/UI/image/bigdata-recommendation.jpg)
基于深度学习 ALS 推荐
![image](https://github.com/HEUer-Way/movie-recommendation-system/blob/master/UI/image/DeepLearning-ALS-recommendation%EF%BC%881%EF%BC%89.jpg)
![image](https://github.com/HEUer-Way/movie-recommendation-system/blob/master/UI/image/DeepLearning-ALS-recommendation%EF%BC%882%EF%BC%89.jpg)
基于 SVD 推荐
![image](https://github.com/HEUer-Way/movie-recommendation-system/blob/master/UI/image/svd-recommendation.jpg)
基于用户推荐
![image](https://github.com/HEUer-Way/movie-recommendation-system/blob/master/UI/image/user-recommendation.jpg)
基于项目推荐
![image](https://github.com/HEUer-Way/movie-recommendation-system/blob/master/UI/image/item-recommendation.jpg)
