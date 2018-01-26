"""
1.线性回归 (Linear Regression)
线性回归是利用连续性变量来估计实际数值（例如房价，呼叫次数和总销售额等）。我们通过线性回归算法找出自变量和因变量间的最佳线性关系，图形上可以确定一条最佳直线。
这条最佳直线就是回归线。这个回归关系可以用Y=aX+b 表示。
我们可以假想一个场景来理解线性回归。比如你让一个五年级的孩子在不问同学具体体重多少的情况下，把班上的同学按照体重从轻到重排队。这个孩子会怎么做呢？
他有可能会通过观察大家的身高和体格来排队。这就是线性回归！这个孩子其实是
认为身高和体格与人的体重有某种相关。而这个关系就像是前一段的Y和X的关系。
在Y=aX+b这个公式里：
	• Y- 因变量
	• a- 斜率
	• X- 自变量
	• b- 截距
a和b可以通过最小化因变量误差的平方和得到（最小二乘法）。
下图中我们得到的线性回归方程是 y=0.2811X+13.9。通过这个方程，我们可以根据一个人的身高得到他的体重信息。
线性回归主要有两种：一元线性回归和多元线性回归。一元线性回归只有一个自变量，而多元线性回归有多个自变量。拟合多元线性回归的时候，可以利用多项式回归（Polynomial Regression）或曲线回归 (Curvilinear Regression)。"""
#Import Library
#Import other necessary libraries like pandas, numpy...
from sklearn import linear_model
#Load Train and Test datasets
#Identify feature and response variable(s) and values must be numeric and numpy arrays

x_train=input_variables_values_training_datasets
y_train=target_variables_values_training_datasets
x_test=input_variables_values_test_datasets

# Create linear regression object
linear = linear_model.LinearRegression()

# Train the model using the training sets and check score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)

#Equation coefficient and Intercept
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

#Predict Output
predicted= linear.predict(x_test)