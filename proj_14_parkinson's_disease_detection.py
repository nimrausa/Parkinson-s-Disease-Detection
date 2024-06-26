# -*- coding: utf-8 -*-
"""Proj 14. Parkinson's Disease Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/148KnrKHmQGMHWQ-t1RgdzZsXQ05cXkg1

Importing the dependencies
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.metrics import accuracy_score



"""Data collection and pre processing"""

#loading the data from csv file to pandas dataframe
parkinson_data= pd.read_csv('/content/parkinsons.csv')

#printing the first five rows of the data frame
parkinson_data.head()

#number of rows and columns in the dataframe
parkinson_data.shape

#getting more information abiut the data
parkinson_data.info()

#checking for the missing values in each column
parkinson_data.isnull().sum()

#getting some statistical measures aboutt the data
parkinson_data.describe()

#distribution of the target variable(status)
parkinson_data['status'].value_counts()

#grouping the data based on the target variables
parkinson_data.groupby('status').mean()

"""Data pre-processing

Separating the features and the target
"""

X=parkinson_data.drop(columns=['name', 'status'], axis=1)
Y=parkinson_data['status']

print(X)

print(Y)

"""Spilitting the dta into the traimimg and the test data"""

X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.2, random_state=2)
print(X.shape,X_train.shape, X_test.shape)

print(X_train)

"""Data standardization"""

scaler=StandardScaler()
scaler.fit(X_train)
X_train=scaler.transform(X_train)
X_test=scaler.transform(X_test)

"""Model training

Support vector machine model
"""

model=svm.SVC(kernel='linear')

#training the SVM model with training data
model.fit(X_train, Y_train)

"""Model evalution"""

#accuracy score on the training data
X_train_prediction= model.predict(X_train)
training_data_accuarcy=accuracy_score(Y_train, X_train_prediction)
print('The train data accuracy',training_data_accuarcy)

#accuracy score on the test data
X_test_prediction= model.predict(X_test)
test_data_accuarcy=accuracy_score(Y_test, X_test_prediction)
print('The test data accuracy',test_data_accuarcy)

"""Building a predictive system"""

input_data = (114.56300,119.16700,86.64700,0.00327,0.00003,0.00146,0.00184,0.00439,0.01185,0.10600,0.00557,0.00721,0.01095,0.01672,0.00703,24.77500,0.555303,0.659132,-6.710219,0.149694,1.913990,0.121777)

#changing the input_data to numoy array
input_data_as_numpy_array= np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)

#standardize the inout data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = model.predict(std_data)
print(prediction)

if (prediction[0]==0):
  print('The person does not have parkinson disease')
else:
  print('The person has parkinson disease')

"""Saving the trained Model"""

import pickle

filename='parkinson_disease.sav'
pickle.dump(model,open(filename,'wb')) #dump=function is used to save the trained model
#wb=writing the file in binary
#classifier=saving the svc model

#loading the saved model
loaded_model=pickle.load(open('parkinson_disease.sav','rb'))
#load=used to load the saved model
#rb=reading the binary format

input_data = (114.56300,119.16700,86.64700,0.00327,0.00003,0.00146,0.00184,0.00439,0.01185,0.10600,0.00557,0.00721,0.01095,0.01672,0.00703,24.77500,0.555303,0.659132,-6.710219,0.149694,1.913990,0.121777)

#changing the input_data to numoy array
input_data_as_numpy_array= np.asarray(input_data)

#reshape the array as we are predicting for one instance
input_data_reshaped= input_data_as_numpy_array.reshape(1,-1)

#standardize the inout data
std_data = scaler.transform(input_data_reshaped)
print(std_data)

prediction = model.predict(std_data)
print(prediction)

if (prediction[0]==0):
  print('The person does not have parkinson disease')
else:
  print('The person has parkinson disease')

for columns in X.columns:
  print(columns)

"""MDVP:Fo(Hz),MDVP:Fhi(Hz),MDVP:Flo(Hz),MDVP:Jitter,MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP,MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE"""