"""
这是一个分类算法。在这个算法中我们将每一个数据作为一个点在一个n维空间上作图（n是特征数），每一个特征值就代表对应坐标值的大小。比如说我们有两个特征：一个人的身高
和发长。我们可以将这两个变量在一个二维空间上作图，图上的每个点都有两个坐标值（这些坐标轴也叫做支持向量）。
现在我们要在图中找到一条直线能最大程度将不同组的点分开。两组数据中距离这条线最近的点到这条线的距离都应该是最远的。
在上图中，黑色的线就是最佳分割线。因为这条线到两组中距它最近的点，点A和B的距离都是最远的。任何其他线必然会使得到其中一个点的距离比这个距离近。这样根据数据点分布在
这条线的哪一边，我们就可以将数据归类。
更多阅读：Simplified Version of Support Vector Machine
我们可以把这个算法想成n维空间里的JezzBall游戏，不过有一些变动：
	• 你可以以任何角度画分割线/分割面（经典游戏中只有垂直和水平方向）。
	• 现在这个游戏的目的是把不同颜色的小球分到不同空间里。
	• 小球是不动的。
"""
#Import Library
from sklearn import svm
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object

model = svm.svc() # there is various option associated with it, this is simple for classification. You can refer link, for mo# re detail.

# Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)

#Predict Output
predicted= model.predict(x_test)