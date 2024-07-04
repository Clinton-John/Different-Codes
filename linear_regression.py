import numpy as np
class Linear_Regression():
  def __init__(self, learning_rate, no_of_iterations): #constructor which gets called every time a new instance of the class is created
    self.learning_rate = learning_rate
    self.no_of_iterations = no_of_iterations


  def fit(self, x, y):
    self.m, self.n = x.shape # shows the available number of rows which are the features and the target
    self.w = np.zeros(self.n) # create an array with zeros having the same number of points as the input data
    self.b =0 # the bias value is initiated as zero
    self.x = x
    self.y = y

      #implementing the Gradient Descent
    for i in range(self.no_of_iterations):
      self.update_weights()

  def update_weights(self):
    y_prediction = self.predict(self.x)

    # calculating the gradients
    dw = - (2 * (self.x.T).dot(self.y - y_prediction)) / self.m
    db = -2 * np.sum(self.y - y_prediction) / self.m

    # updating the values after each iteration
    self.w = self.w - self.learning_rate*dw
    self.b = self.b - self.learning_rate*db

    #in this function, x is the years of experience of an individual and is given into the function, and it is incharge of predicting the salary
  def predict(self, x):
    return x.dot(self.w) + self.b

