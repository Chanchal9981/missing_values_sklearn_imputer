# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer

train=pd.read_csv("C:\\Users\\patid\\Downloads\\train (2).csv")
test=pd.read_csv("C:\\Users\\patid\\Downloads\\test (1).csv")
print("shape of train_data is=",train.shape)
print("shape of test_data is=",test.shape)

train.head()

X_train=train.drop("SalePrice",axis=1)
y_train=train["SalePrice"]
print("shape of X_train is=",X_train.shape)
print("shape of y_train is=",y_train.shape)

num_vars=X_train.select_dtypes(include=["int64","float64"]).columns
num_vars

X_train[num_vars].isnull().sum()

#fill missing value manually then  we use 
#imputer_mean=SimpleImputer(strategy='constant',fill_value=1)
imputer_mean=SimpleImputer(strategy='mean')
imputer_mean.fit(X_train[num_vars])

imputer_mean.statistics_

imputer_mean.transform(X_train[num_vars])

X_train[num_vars]=imputer_mean.transform(X_train[num_vars])
test[num_vars]=imputer_mean.transform(test[num_vars])

X_train[num_vars].isnull().sum().sum()

test[num_vars].isnull().sum().sum()

"""# catagorical data imputation"""

cat_vars=X_train.select_dtypes(include=["object"]).columns
cat_vars

X_train[cat_vars].isnull().sum()

imputer_mode=SimpleImputer(strategy="most_frequent")
imputer_mode.fit(X_train[cat_vars])

X_train[cat_vars]=imputer_mode.transform(X_train[cat_vars])
test[cat_vars]=imputer_mode.transform(test[cat_vars])

X_train[cat_vars].isnull().sum().sum()

test[cat_vars].isnull().sum().sum()

#to see which value are impute in cat data
imputer_mode.statistics_

