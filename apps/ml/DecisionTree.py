"""这是我最喜欢也是能经常使用到的算法。它属于监督式学习，常用来解决分类问题。令人惊讶的是，它既可以运用于类别变量（categorical variables）也可以作用于连续变量。
这个算法可以让我们把一个总体分为两个或多个群组。分组根据能够区分总体的最重要的特征变量/自变量进行。更详细的内容可以阅读这篇文章Decision Tree Simplified。
从上图中我们可以看出，总体人群最终在玩与否的事件上被分成了四个群组。而分组是依据一些特征变量实现的。用来分组的具体指标有很多，比如Gini，information Gain,
Chi-square,entropy。
理解决策树原理的最好的办法就是玩Jezzball游戏。这是微软的一款经典游戏（见下图）。这个游戏的最终任务是在一个有移动墙壁的房间里，通过建造墙壁来尽可能地将房间分
成尽量大的，没有小球的空间。
每一次你用建墙来分割房间，其实就是在将一个总体分成两部分。决策树也是用类似方法将总体分成尽量多的不同组别。"""

#Import Library
#Import other necessary libraries like pandas, numpy...

from sklearn import tree
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset

# Create tree object
model = tree.DecisionTreeClassifier(criterion='gini') # for classification, here you can change the algorithm as gini or entropy (information gain) by default it is gini

# model = tree.DecisionTreeRegressor() for regression

# Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)

#Predict Output
predicted= model.predict(x_test)