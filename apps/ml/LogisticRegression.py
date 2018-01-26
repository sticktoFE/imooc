"""
2.逻辑回归
别被它的名字迷惑了，逻辑回归其实是一个分类算法而不是回归算法。通常是利用已知的自变量来预测一个离散型因变量的值（像二进制值0/1，是/否，真/假）。简单来说，
它就是通过拟合一个逻辑函数（logit fuction）来预测一个事件发生的概率。所以它预测的是一个概率值，自然，它的输出值应该在0到1之间。
同样，我们可以用一个例子来理解这个算法。
假设你的一个朋友让你回答一道题。可能的结果只有两种：你答对了或没有答对。为了研究你最擅长的题目领域，你做了各种领域的题目。那么这个研究的结果可能是这样的：
如果是一道十年级的三角函数题，你有70%的可能性能解出它。但如果是一道五年级的历史题，你会的概率可能只有30%。逻辑回归就是给你这样的概率结果。
回到数学上，事件结果的胜算对数（log odds）可以用预测变量的线性组合来描述：
odds= p/ (1-p) = probability of event occurrence / probability of not event occurrence
ln(odds) = ln(p/(1-p))
logit(p) = ln(p/(1-p)) = b0+b1X1+b2X2+b3X3....+bkXk
在这里，p 是我们感兴趣的事件出现的概率。它通过筛选出特定参数值使得观察到的样本值出现的概率最大化，来估计参数，而不是像普通回归那样最小化误差的平方和。
你可能会问为什么需要做对数呢？简单来说这是重复阶梯函数的最佳方法。因本篇文章旨不在此，这方面就不做详细介绍了。

"""
#Import Library
from sklearn.linear_model import LogisticRegression
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset

# Create logistic regression object

model = LogisticRegression()

# Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)

#Equation coefficient and Intercept
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)

#Predict Output
predicted= model.predict(x_test)