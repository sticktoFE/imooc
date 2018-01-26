"""
这个算法是建立在贝叶斯理论上的分类方法。它的假设条件是自变量之间相互独立。简言之，朴素贝叶斯假定某一特征的出现与其它特征无关。比如说，如果一个水果它是红色的，
圆状的，直径大概7cm左右，我们可能猜测它为苹果。即使这些特征之间存在一定关系，在朴素贝叶斯算法中我们都认为红色，圆状和直径在判断一个水果是苹果的可能性上是相互独立的。
朴素贝叶斯的模型易于建造，并且在分析大量数据问题时效率很高。虽然模型简单，但很多情况下工作得比非常复杂的分类方法还要好。
贝叶斯理论告诉我们如何从先验概率P(c),P(x)和条件概率P(x|c)中计算后验概率P(c|x)。算法如下：

	• P(c|x)是已知特征x而分类为c的后验概率。
	• P(c)是种类c的先验概率。
	• P(x|c)是种类c具有特征x的可能性。
	• P(x)是特征x的先验概率。
例子： 以下这组训练集包括了天气变量和目标变量“是否出去玩”。我们现在需要根据天气情况将人们分为两组：玩或不玩。整个过程按照如下步骤进行：
步骤1：根据已知数据做频率表
步骤2：计算各个情况的概率制作概率表。比如阴天（Overcast）的概率为0.29，此时玩的概率为0.64.
步骤3：用朴素贝叶斯计算每种天气情况下玩和不玩的后验概率。概率大的结果为预测值。
提问: 天气晴朗的情况下(sunny)，人们会玩。这句陈述是否正确？
我们可以用上述方法回答这个问题。P(Yes | Sunny)=P(Sunny | Yes) * P(Yes) / P(Sunny)。
这里，P(Sunny |Yes) = 3/9 = 0.33, P(Sunny) = 5/14 = 0.36, P(Yes)= 9/14 = 0.64。
那么，P (Yes | Sunny) = 0.33 * 0.64 / 0.36 = 0.60>0.5,说明这个概率值更大。
当有多种类别和多种特征时，预测的方法相似。朴素贝叶斯通常用于文本分类和多类别分类问题。"""
#Import Library
from sklearn.naive_bayes import GaussianNB
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset

# Create SVM classification object
model = GaussianNB() # there is other distribution for multinomial classes like Bernoulli Naive Bayes, Refer link

# Train the model using the training sets and check score
model.fit(X, y)

#Predict Output
predicted= model.predict(x_test)