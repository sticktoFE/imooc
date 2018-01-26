"""
随机森林是对决策树集合的特有名称。随机森林里我们有多个决策树（所以叫“森林”）。为了给一个新的观察值分类，根据它的特征，每一个决策树都会给出一个分类。随机森林算法
选出投票最多的分类作为分类结果。
怎样生成决策树：
	1. 如果训练集中有N种类别，则有重复地随机选取N个样本。这些样本将组成培养决策树的训练集。
	2. 如果有M个特征变量，那么选取数m << M，从而在每个节点上随机选取m个特征变量来分割该节点。m在整个森林养成中保持不变。
	3. 每个决策树都最大程度上进行分割，没有剪枝。

"""
#Import Library
from sklearn.ensemble import RandomForestClassifier
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset

# Create Random Forest object
model= RandomForestClassifier()

# Train the model using the training sets and check score
model.fit(X, y)

#Predict Output
predicted= model.predict(x_test)