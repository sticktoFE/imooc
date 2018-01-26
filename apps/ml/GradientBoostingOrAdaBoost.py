"""
GBM和AdaBoost都是在有大量数据时提高预测准确度的boosting算法。Boosting是一种集成学习方法。
它通过有序结合多个较弱的分类器/估测器的估计结果来提高预测准确度。这些boosting算法在Kaggle，
AV Hackthon, CrowdAnalytix等数据科学竞赛中有出色发挥。
"""
#Import Library
from sklearn.ensemble import GradientBoostingClassifier
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create Gradient Boosting Classifier object
model= GradientBoostingClassifier(n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0)
# Train the model using the training sets and check score
model.fit(X, y)
#Predict Output
predicted= model.predict(x_test)
