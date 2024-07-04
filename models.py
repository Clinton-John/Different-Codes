import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns

insurance_data = pd.read_csv('insurance.csv')

insurance_data.head()
insurance_data.shape
insurance_data.describe()


insurance_data.replace({'sex':{'male':0, 'female':1}}, inplace=True)

# the smoker column
insurance_data.replace({'smoker':{'yes':0, 'no':1}}, inplace=True)

# the region column
insurance_data.replace({'region':{'southeast':0, 'southwest':1, 'northeast':2, 'northwest':3}}, inplace=True)

#separating the target from the features columns
X = insurance_data.drop(columns='charges', axis=1)
Y = insurance_data['charges']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
regressor = LinearRegression()

regressor.fit(X_train, Y_train)

#predicting using the training data before using the testing data
training_data_prediction = regressor.predict(X_train)

#the R Squared Value
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared value : ', r2_train)
# if the value is close to one then the chances of accuracy in the model is high

# predicting using the testing data
testing_data_prediction = regressor.predict(X_test)

r2_test = metrics.r2_score(Y_test, testing_data_prediction)
print('R squared value : ', r2_test)