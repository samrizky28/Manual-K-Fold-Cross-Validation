import pandas as pd
import math

#X is the independent variable in the dataset
#y is the target variable
#n is the number of observations in the dataset

n=len(X)

#Let say we want to make 5-fold CV. It means, we are equivalent to doing a 20% separation of test data, then:
fold1 = math.ceil(0.2*n)
fold2 = math.ceil(0.4*n)
fold3 = math.ceil(0.6*n)
fold4 = math.ceil(0.8*n)
fold5 = n

#So splitting the dataset into training data and testing data becomes:
#1st fold
X_train_cv1 = X[fold1:n]
X_test_cv1 = X[test_cv[0][0]:fold1]
y_train_cv1 = y[fold1:n]
y_test_cv1 = y[test_cv[0][0]:fold1]
#2nd fold
X_train_cv2 = pd.concat([X[train_cv[1][0]:fold1], X[fold2:n]])
X_test_cv2 = X[fold1:fold2]
y_train_cv2 = pd.concat([y[train_cv[1][0]:fold1], y[fold2:n]])
y_test_cv2 = y[fold1:fold2]
#3rd fold
X_train_cv3 = pd.concat([X[train_cv[2][0]:fold2], X[fold3:n]])
X_test_cv3 = X[fold2:fold3]
y_train_cv3 = pd.concat([y[train_cv[2][0]:fold2], y[fold3:n]])
y_test_cv3 = y[fold2:fold3]
#4th fold
X_train_cv4 = pd.concat([X[train_cv[3][0]:fold3], X[fold4:n]])
X_test_cv4 = X[fold3:fold4]
y_train_cv4 = pd.concat([y[train_cv[3][0]:fold3], y[fold4:n]])
y_test_cv4 = y[fold3:fold4]
#5th fold
X_train_cv5 = X[train_cv[4][0]:fold4]
X_test_cv5 = X[fold4:fold5]
y_train_cv5 = y[train_cv[4][0]:fold4]
y_test_cv5 = y[fold4:fold5]
