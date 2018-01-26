"""
独热编码
"""
#Import Library
#Import other necessary libraries like pandas, numpy...

from sklearn import preprocessing
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset

# Create tree object
encoder = preprocessing.OneHotEncoder() # for classification, here you can change the algorithm as gini or entropy (information gain) by default it is gini
encoder.fit([[0,2,1,12],
             [1,3,5,3],
             [2,3,2,12],
             [1,2,4,3]])
encoded_vector=encoder.transform([[2,3,5,3]])
if __name__ == '__main__':
    print("\nEncoded vector="+encoded_vector)

