"""
9.降维算法（Dimensionality Reduction Algorithms）
在过去的4-5年里，可获取的数据几乎以指数形式增长。公司/政府机构/研究组织不仅有了更多的数据来源，也获得了更多维度的数据信息。
例如：电子商务公司有了顾客更多的细节信息，像个人信息，网络浏览历史，个人喜恶，购买记录，反馈信息等，他们关注你的私人特征，
比你天天去的超市里的店员更了解你。
作为一名数据科学家，我们手上的数据有非常多的特征。虽然这听起来有利于建立更强大精准的模型，但它们有时候反倒也是建模中的一大难题。
怎样才能从1000或2000个变量里找到最重要的变量呢？这种情况下降维算法及其他算法，如决策树，随机森林，PCA，因子分析，相关矩阵，
和缺省值比例等，就能帮我们解决难题。
进一步的了解可以阅读Beginners Guide To Learn Dimension Reduction Techniques
(https://www.analyticsvidhya.com/blog/2015/07/dimension-reduction-methods/)
"""
#Import Library
from sklearn import decomposition
#Assumed you have training and test data set as train and test
# Create PCA obeject
pca= decomposition.PCA(n_components=k) #default value of k =min(n_sample, n_features)
# For Factor analysis
#fa= decomposition.FactorAnalysis()
# Reduced the dimension of training dataset using PCA

train_reduced = pca.fit_transform(train)

#Reduced the dimension of test dataset
test_reduced = pca.transform(test)