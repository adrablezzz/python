import json
def pt(x):
  with open("output.txt", "w") as f:
    print(json.dumps(x.tolist()), file=f)

# 1. 工具库
# 1.1 Numpy
import numpy as np 
# 创建多维数组
x = np.array([[1,2,3], [4,5,6]])
print('x:\n', x)

# 1.2 Scipy
from scipy import sparse
# 创建一个二维Numpy数组,对角线为1,其余为0
eye = np.eye(4)
print('eye:\n', eye)

# 将Numpy数组转化为CSR格式的Scipy稀疏矩阵
# 只保留非零元素
sparse_matrix = sparse.csr_matrix(eye)
print('Scipy parse CSR matrix:\n', sparse_matrix)

# 创建COO格式的稀疏矩阵
data = np.ones(4)
row_indices = np.arange(4)
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
print('COO格式稀疏矩阵:\n', eye_coo)

# 1.3 matplotlib
import matplotlib.pyplot as plt
# 在-10和10之间生成一个数列，共100个数
x = np.linspace(-10, 10, 100)
# 用正弦函数创建第二个数组
y = np.sin(x)
# plot绘制一个数组关于另一个数组的折线图
# plt.plot(x, y, marker='x')
# plt.show()

# 1.4 pandas
import pandas as pd
data = {
  'name': ['Zhangsan', 'Lisi', 'Wangwu'],
  'age': [20, 21, 22],
  'address': ['Zhejiang', 'Chongqing', 'Guizhou']
}
data_pandas = pd.DataFrame(data)
print('data_pandas:\n', data_pandas)
# 打印年龄打印？的
print('data_pandas age > 20:\n', data_pandas[data_pandas.age > 20])

# 1.5 mglearn
import mglearn

# 2.第一个应用：鸢尾花分类
# 2.1 鸢尾花数据
from sklearn.datasets import load_iris
iris_dataset = load_iris()
print('iris_dataset keys:\n', iris_dataset.keys())
# print(iris_dataset['DESCR'][:193]+'\n...')
# 花的品种
print('target_names:',iris_dataset['target_names'])
'''
花的特征:
  sepal length (cm), sepal width (cm), petal length (cm), petal width (cm)
  花萼长度 花萼宽度 花瓣长度 花瓣宽度
'''
print('feature_names:',iris_dataset['feature_names'])
# 花的数据: 一行代表一朵花，列依次对应特征
print('data',iris_dataset['data'])
# 数据形状
print('shape of data:', iris_dataset['data'].shape)
# target 0-2对应花的品种
print('target:', iris_dataset['target'])


# 2.2 训练数据和测试数据
# 将总的数据随机分成训练数据和测试数据 75%:25%
from sklearn.model_selection import train_test_split
# 训练数据 测试数据 训练标签 测试标签
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
print('X_train shape:', X_train.shape)
print('y_train shape:', y_train.shape)
print('X_test shape:', X_test.shape)
print('y_test shape:', y_test.shape)


# 2.3 观察数据
# 绘制散点图或散点图矩阵
# iris_dataframe = pd.DataFrame(X_train, columns=iris_dataset.feature_names)
# pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15,15), marker='0', hist_kwds={'bins':20}, s=60, alpha=.8, cmap=mglearn.cm3)
# plt.show()

# 2.4 K近邻算法
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# 2.5 做出预测
X_new = np.array([[5, 2.9, 1, 0.2]])
print('X_new shape:', X_new.shape)
prediction = knn.predict(X_new)
print('prediction:', prediction)
print('flower race is:', iris_dataset['target_names'][prediction])

# 2.6 评估模型
# 测试数据种类
y_pred = knn.predict(X_test)
print('test prediction:\n', y_pred)
# 计算精度
print('Test set score: {:.2f}'.format(np.mean(y_pred == y_test)))
# 也可以用knn.score方法计算精度
print('Test set score by knn.score: {:.2f}'.format(knn.score(X_test, y_test)))

# 2.7小结
'''
任务：利用鸢尾花的测量数据来预测其品种
品种：setosa versicolor virginica 对应 0 1 2
在分类问题中，可能的品种被称为类别，每朵花的品种被称为它的标签
数据集:(包含两个Numpy数组)
  X: 包含数据(特征的二维数组，每个数据点对应一行，每个特征对应一列)
  y: 正确输出或预期输出(一维数组，包含一个类别标签，每个样本都是0到2的整数)
数据集分为：
  训练集(training set):用于构建模型
  测试集(test set):用于评估模型
K近邻分类算法(KNeighborsClassifier):
  1.将类实例化并设定参数;用fit来构建模型:(X_train训练数据,y_train训练输出)
  2.用score方法评估模型
必需代码:
  X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)
  knn = KNeighborsClassifier(n_neighbors=1)
  knn.fit(X_train, y_train)
  print('Test set score by knn.score: {:.2f}'.format(knn.score(X_test, y_test)))
'''

# 3.监督学习
# 3.1 分类与回归
'''
分类问题的目标是预测类别标签
分类问题可分为：
  二分类：正类和反类(如：邮件是否垃圾邮件？)
  多分类(如：鸢尾花问题)
回归任务的目标是预测一个连续值(浮点数/实数)
(如：根据教育水平、年龄和居住地预测一个人年收入)
区分分类和回归：输出是否具有连续性
'''
# 3.2 泛化、过拟合和欠拟合
'''
泛化：一个模型对没有见过的数据做出准确预测，即称为改模型可以从训练集泛化到测试集
过拟合：过分关注模型细节，导致模型复杂
欠拟合：与过拟合相反
'''
# 3.3 监督学习算法
# 3.3.1 样本数据集
# forge二分类数据集
# 生成数据集 forge
'''
X[:, 0]表示对Numpy数组X第一个维度取所有，第二个维度取第0个索引的数据
X = Numpy([[1,2],[3,4],[5,6]])
X[:, 0] => [1, 3, 5]
'''
# X, y = mglearn.datasets.make_forge()
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# plt.legend(['Class 0', 'Class 1'], loc=4)
# plt.xlabel('First feature')
# plt.ylabel('Second feature')
# plt.show()
# print('X.shape:', X.shape)
# wave数据集演示回归算法
# X, y = mglearn.datasets.make_wave(n_samples=40)
# plt.plot(X, y, 'o')
# plt.ylim(-3, 3)
# plt.xlabel('Feature')
# plt.ylabel('Target')
# plt.show()
# 乳腺癌数据集(分类:良性/恶性)
# from sklearn.datasets import load_breast_cancer
# cancel = load_breast_cancer()
# print('cancel.keys:\n{}'.format(cancel.keys()))
# print('cancel data.shape:\n{}'.format(cancel.data.shape))
# print('Sample count per class:{}'.format({n:v for n, v in zip(cancel.target_names, np.bincount(cancel.target))}))
# print('cancel feature_names:\n{}'.format(cancel.feature_names))
# 波士顿房价数据集(回归) removed
# from sklearn.datasets import load_boston
# boston = load_boston()
# print('boston data.shape:{}'.format(boston.data.shape))

# 3.3.2 k近邻
# 3.3.2.1 k近邻分类
# 1个邻居
# X, y = mglearn.datasets.make_forge()
# mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
# # mglearn.plots.plot_knn_classification(n_neighbors=1)
# mglearn.plots.plot_knn_classification(n_neighbors=3)
# plt.legend(['Class 0', 'Class 1'], loc=4)
# plt.xlabel('First feature')
# plt.ylabel('Second feature')
# plt.show()
# print('X.shape:', X.shape)
# scikit-learn应用k近邻算法
from sklearn.model_selection import train_test_split
X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
# 调用predict对测试数据集进行预测
print('k neighbors clf.predict: {}'.format(clf.predict(X_test)))
# 评估模型
print('clf.score: {:.2f}'.format(clf.score(X_test, y_test)))
# 分析KNeighborsClassifier 决策边界
# fig, axes = plt.subplots(1, 3, figsize=(10, 3))
# for n_neigbors, ax in zip([1, 3, 9], axes):
#   clf = KNeighborsClassifier(n_neighbors=n_neigbors).fit(X, y)
#   mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=.5, ax=ax, alpha=.4)
#   mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
#   ax.set_title('{} neighbor(s)'.format(n_neigbors))
#   ax.set_xlabel('feature 0')
#   ax.set_ylabel('feature 1')
# axes[0].legend(loc=3)
# plt.show()
#  模型精度 乳腺癌数据集例
# from sklearn.datasets import load_breast_cancer
# cancel = load_breast_cancer()
# X_train, X_test, y_train, y_test = train_test_split(cancel.data, cancel.target, stratify=cancel.target, random_state=66)
# train_accuracy = []
# test_accuracy = []
# neighbors_settings = range(1, 11)
# for n_neighbors in neighbors_settings:
#   clf = KNeighborsClassifier(n_neighbors=n_neighbors)
#   clf.fit(X_train, y_train)
#   train_accuracy.append(clf.score(X_train, y_train))
#   test_accuracy.append(clf.score(X_test, y_test))
# plt.plot(neighbors_settings, train_accuracy, label='train_accuracy')
# plt.plot(neighbors_settings, test_accuracy, label='test_accuracy')
# plt.ylabel('Accuracy')
# plt.xlabel('n_neighbors')
# plt.legend()
# plt.show()
# 3.3.2.2 k紧邻回归
# mglearn.plots.plot_knn_regression(n_neighbors=1)
# plt.show()
# k紧邻算法在scikit-learn的KNeighborsRegress类中实现
from sklearn.neighbors import KNeighborsRegressor
X, y = mglearn.datasets.make_wave(n_samples=40)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
reg = KNeighborsRegressor(n_neighbors=3)
reg.fit(X_train, y_train)
print('reg test predictions: {}'.format(reg.predict(X_test)))
# score返回R^2分数(拟合度)
print('reg test R^2: {:.2f}'.format(reg.score(X_test, y_test)))
# 3.3.2.3 分析KNeighborsRegressor略
# 3.3.2.4 优点、缺点和参数
'''
参数：邻居个数和数据点之间距离的度量方法
K-NN优点：容易理解
k-NN缺点：对于很多特征的数据集效果不好；尤其是大多数特征取0的数据集(稀疏数据集)
'''

# 3.3.3 线性模型
# 3.3.3.1用于回归的线性模型
'''
y = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b
x[?]表示单个数据点的特征；w和b是学习模型的参数；y是模型的预测结果
单一特征的数据集模型：
y = w[0] * x[0] + b 
'''
# mglearn.plots.plot_linear_regression_wave()
# plt.show()
# 3.3.3.2 线性回归(最小二乘法)
from sklearn.linear_model import LinearRegression
X, y = mglearn.datasets.make_wave(n_samples=60)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
lr = LinearRegression().fit(X_train, y_train)
print('斜率lr.coef_: {}'.format(lr.coef_))
print('截距lr.intercept_: {}'.format(lr.intercept_))
print('train set score: {:.2f}'.format(lr.score(X_train, y_train)))
print('test set score: {:.2f}'.format(lr.score(X_test, y_test)))
# print('X_train: {}, y_train: {}, X_test: {}, y_test: {}'.format(X_train.shape, y_train.shape, X_test.shape, y_test.shape))
# boston略
# 3.3.3.3 岭回归 linear_model.Ridge 
# 与最小二乘法相同，只是要求系数w尽可能小
from sklearn.linear_model import Ridge
ridge = Ridge(alpha=1).fit(X_train, y_train) # wave数据集；alpha模型简单性和训练程度参数默认1
print('ridge train score: {:.2f}'.format(ridge.score(X_train, y_train)))
print('ridge test score: {:.2f}'.format(ridge.score(X_test, y_test)))
# alpha值的影响
''' fail
plt.plot(ridge.coef_, 's', label='Ridge alpha=1')
plt.plot(ridge.coef_, '^', label='Ridge alpha=10')
plt.plot(ridge.coef_, 'v', label='Ridge alpha=0.1')
plt.plot(lr.coef_, 'o', label='LinearRegression')
plt.xlabel('Coefficient index')
plt.ylabel('Coefficient magnitude')
plt.hlines(0, 0, len(lr.coef_))
plt.ylim(-25, 25)
plt.legend()
plt.show()
'''
# 学习曲线
# mglearn.plots.plot_ridge_n_samples()
# plt.show()

# 3.3.3.4 lasso 正则化的线性回归
'''
与岭回归相同，lasso也是约束系数使其接近于0，但使用L1正则化方法
L1正则化结果：使用L1时某些系数刚好为0(这说明某些特征被模型完全忽略)
lasso应用到boston房价数据集上，略
'''
# 3.3.3.5 用于分类的线性模型
'''
预测：y = w[0] * x[0] + w[1] * x[1] + ... + w[p] * x[p] + b > 0
最常见的两种分类算法：
  Logistic回归(linear_model.LogisticRegression) 
  线性支持向量机(linear support vector machine, 线性SVM)
略
'''
# 3.3.3.6 用于多分类的线性模型 略

# 3.3.4 朴素贝叶斯分类器
'''
与线性模型相似，训练速度更快，泛化性稍差
不理解
'''
def fun54():
  X = np.array([
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
  ])
  y = np.array([0, 1, 0, 1])
  counts = {}
  for label in np.unique(y):
    # X第一列以 0 1 分类求和 
    counts[label] = X[y==label].sum(axis=0)
  print('Feature counts: \n{}'.format(counts))
# fun54()

# 3.3.5 决策树
'''
本质是通过大量if/else学习判断
'''
def fun55():
  from sklearn.datasets import load_breast_cancer
  from sklearn.tree import DecisionTreeClassifier
  cancer = load_breast_cancer()
  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, stratify=cancer.target, random_state=42)
  # 剪枝:设置max_depth,提高模型泛化度
  tree = DecisionTreeClassifier(max_depth=4,random_state=0)
  tree.fit(X_train, y_train)
  print('Accuracy on train set: {:.3f}'.format(tree.score(X_train, y_train)))
  print('Accuracy on test set:  {:.3f}'.format(tree.score(X_test, y_test)))
  from sklearn.tree import export_graphviz
  export_graphviz(tree, out_file='tree.dot', class_names=['malignant', 'benign'], feature_names=cancer.feature_names, impurity=False, filled=True)
  # 安装graphviz可视化显示 略
  # 树的特征重要性
  print('Feature importance: \n{}'.format(tree.feature_importances_))
# fun55()

# 3.3.6 决策树集成
'''
随机森林：构造多颗决策树，取平均值
梯度提升决策树: 合并多个决策树来构建更为强大的模型
优先随机森林，如果预测时间太长或对模型进度小数点后第二位提升也很重要，切换梯度提升
'''
def fun56():
  from sklearn.ensemble import RandomForestClassifier
  from sklearn.datasets import make_moons
  X, y = make_moons(n_samples=100, noise=0.25, random_state=3)
  X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
  forest = RandomForestClassifier(n_estimators=5, random_state=2)
  forest.fit(X_train, y_train)
  # 可视化
  fig, axes = plt.subplots(2, 3, figsize=(20, 10))
  for i, (ax, tree) in enumerate(zip(axes.ravel(), forest.estimators_)):
    ax.set_title('Tree {}'.format(i))
    mglearn.plots.plot_tree_partition(X_train, y_train, tree, ax=ax)
  mglearn.plots.plot_2d_separator(forest, X_train, fill=True, ax=axes[-1, -1], alpha=.4)
  axes[-1, -1].set_title('Random Forest')
  mglearn.discrete_scatter(X_train[:, 0], X_train[:, 1], y_train)
  plt.show()
# fun56()
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
cancer = load_breast_cancer()
def fun70():
  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
  forest = RandomForestClassifier(n_estimators=100, random_state=0)
  forest.fit(X_train, y_train)
  print('Accuracy on train set: {:.3f}'.format(forest.score(X_train, y_train)))
  print('Accuracy on test set: {:.3f}'.format(forest.score(X_test, y_test)))
  def plot_feature_importances_cancer(model):
    n_features = cancer.data.shape[1]
    plt.barh(range(n_features),model.feature_importances_,align='center')
    plt.yticks(np.arange(n_features),cancer.feature_names)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature")
    plt.show()
  plot_feature_importances_cancer(forest)
# fun70()
# 梯度提升决策树
def fun72():
  from sklearn.ensemble import GradientBoostingClassifier
  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
  # gbrt = GradientBoostingClassifier(random_state=0, max_depth=1) #剪枝
  gbrt = GradientBoostingClassifier(random_state=0, learning_rate=0.01) #也可以降低学习率
  gbrt.fit(X_train, y_train)
  print('Accuracy on gbrt train set: {:.3f}'.format(gbrt.score(X_train, y_train)))
  print('Accuracy on gbrt test set: {:.3f}'.format(gbrt.score(X_test, y_test)))
# fun72()

# 3.3.7 核支持向量机 SVM
from sklearn.datasets import make_blobs
def fun75():
  X, y = make_blobs(centers=4, random_state=8)
  y = y % 2
  mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
  plt.xlabel('Feature 0')
  plt.ylabel('Feature 1')
  plt.show()
# fun75()
# 线性SVM给出决策边界
from sklearn.svm import LinearSVC
def fun76():
  X, y = make_blobs(centers=4, random_state=8)
  y = y % 2
  linear_svm = LinearSVC().fit(X, y)
  mglearn.plots.plot_2d_separator(linear_svm, X)
  mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
  plt.xlabel('Feature 0')
  plt.ylabel('Feature 1')
  plt.show()
# fun76()
# 拓展：添加第二特征的平方
from mpl_toolkits.mplot3d import Axes3D, axes3d
def fun77():
  X, y = make_blobs(centers=4, random_state=8)
  y = y % 2
  X_new = np.hstack([X, X[:, 1:] ** 2])
  figure = plt.figure()
  # 3d可视化
  ax = Axes3D(figure, elev=-152, azim=-26, auto_add_to_figure=False)
  figure.add_axes(ax)
  # # 先画出y=0的点，再画出y=1的点
  mask = y == 0 # mask数组内的值x依次执行x==0 -> mask=[False,True...]
  ax.scatter(X_new[mask, 0], X_new[mask, 1], X_new[mask, 2], c='b', cmap=mglearn.cm2, s=60, edgecolor='k')
  ax.scatter(X_new[~mask, 0], X_new[~mask, 1], X_new[~mask, 2], c='r', marker='^', cmap=mglearn.cm2, s=60, edgecolor='k')
  ax.set_xlabel("feature0")
  ax.set_ylabel("feature1")
  ax.set_zlabel("feature1**2")
  plt.show()
# fun77()
# svm_3d显示决策边界
def fun78():
  X, y = make_blobs(centers=4, random_state=8)
  y = y % 2
  X_new = np.hstack([X, X[:, 1:] ** 2])
  liner_3d_svm = LinearSVC().fit(X_new, y)
  coef, intercept = liner_3d_svm.coef_.ravel(), liner_3d_svm.intercept_

  figure = plt.figure()
  # 3d可视化
  ax = Axes3D(figure, elev=-152, azim=-26, auto_add_to_figure=False)
  figure.add_axes(ax)
  xx = np.linspace(X_new[:, 0].min() - 2, X_new[:, 0].max() + 2, 50)
  yy = np.linspace(X_new[:, 1].min() - 2, X_new[:, 1].max() + 2, 50)
  XX, YY = np.meshgrid(xx, yy)
  ZZ = (coef[0] * XX + coef[1] * YY + intercept) / -coef[2]
  ax.plot_surface(XX, YY, ZZ, rstride=8, cstride=8, alpha=0.3)
  # # 先画出y=0的点，再画出y=1的点
  mask = y == 0 # mask数组内的值x依次执行x==0 -> mask=[False,True...]
  ax.scatter(X_new[mask, 0], X_new[mask, 1], X_new[mask, 2], c='b', cmap=mglearn.cm2, s=60, edgecolor='k')
  ax.scatter(X_new[~mask, 0], X_new[~mask, 1], X_new[~mask, 2], c='r', marker='^', cmap=mglearn.cm2, s=60, edgecolor='k')
  ax.set_xlabel("feature0")
  ax.set_ylabel("feature1")
  ax.set_zlabel("feature1**2")
  plt.show()
# fun78()
# 理解SVM
'''
数据点之间的距离，高斯核：k(x1,x2) = exp(-γ ||x1-x2||^2)
x1,x2是数据点，||x1-x2||是欧式距离，γ是控制高斯核宽度参数
'''
from sklearn.svm import SVC
def fun81():
  X, y = mglearn.tools.make_handcrafted_dataset()
  svm = SVC(kernel='rbf', C=10, gamma=0.1).fit(X, y)
  mglearn.plots.plot_2d_separator(svm, X, eps=.5)
  mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
  # 画出支持向量
  sv = svm.support_vectors_
  # 支持向量的类别标签由dual_coef_的正负号给出
  sv_labels = svm.dual_coef_.ravel() > 0
  mglearn.discrete_scatter(sv[:, 0], sv[:, 1], sv_labels, s=15, markeredgewidth=3)
  plt.xlabel('Feature 0')
  plt.ylabel('Feature1')
  plt.show()
# fun81()
def fun82():
  fig, axes = plt.subplots(3, 3, figsize=(15, 10))
  for ax, C in zip(axes, [-1, 0, 3]):
    for a, gamma in zip(ax, range(-1, 2)):
      mglearn.plots.plot_svm(log_C=C, log_gamma=gamma, ax=a)
  axes[0, 0].legend(['class 0', 'class 1', 'sv class 0', 'sv class 1'], ncol=4, loc=(.9, 1.2))
  plt.show()
  # C越大决策性越弯曲越精确，γ越大越关注单个点
  # 默认C=1，γ=1/n_features
# fun82()
def fun83():
  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
  svc = SVC()
  svc.fit(X_train, y_train)
  print('Accuracy on svc train: {:.2f}'.format(svc.score(X_train, y_train)))
  print('Accuracy on svc test: {:.2f}'.format(svc.score(X_test, y_test)))

  plt.plot(X_train.min(axis=0), 'o', label="min")
  plt.plot(X_train.max(axis=0), '^', label="max")
  plt.legend(loc=4)
  plt.xlabel('Feature index')
  plt.ylabel('Feature magnitude')
  plt.yscale('log')
  plt.show()
# fun83()
def fun84():
  X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=0)
  # 计算训练集中每个特征的最小值
  min_on_training = X_train.min(axis=0) #二维数组的，axis0表示每列，1表示每行
  # 计算训练集中每个特征的范围（最大值-最小值）
  range_on_training = (X_train - min_on_training).max(axis=0)
  # 二维数组-一维数组 = 二维数组的第一个维度的元素的相同索引子元素-一维数组对应索引元素
  # 减去最小值，然后除以范围
  # 这样每个特征都是min=0和max=1
  X_train_scaled = (X_train - min_on_training) / range_on_training
  print("Minimum for each feature\n{}".format(X_train_scaled.min(axis=0)))
  print("Maximum for each feature\n {}".format(X_train_scaled.max(axis=0)))
  # 利用训练集的最小值和范围对测试集做相同的变换
  X_test_scaled = (X_test - min_on_training) / range_on_training
  svc = SVC()
  svc.fit(X_train_scaled, y_train)
  print("Accuracy on training set: {:.3f}".format(svc.score(X_train_scaled, y_train)))
  print("Accuracy on test set: {:.3f}".format(svc.score(X_test_scaled, y_test)))
# fun84()