"""
Implement the linear regression model using python and numpy in the following class.
The method fit() should take inputs like,
x = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

import numpy

class LinearRegression(object):
  """
  An implementation of linear regression model
  """
 
 
 
  
  def fit(_input, _output):
      x=_input
      y=_output
      def mean(values):
	        return sum(values) / float(len(values))
 
      # Calculate covariance between x and y
      def covariance(x, mean_x, y, mean_y):
	        covar = 0.0
	        for i in range(len(x)):
			covar += (x[i] - mean_x) * (y[i] - mean_y)
	        return covar
 
      # Calculate the variance of a list of numbers
      def variance(values, mean):
	        return sum([(x-mean)**2 for x in values])
 
       # Calculate coefficients

	   x_mean, y_mean = mean(x), mean(y)
	   b1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
	   b0 = y_mean - b1 * x_mean
	   return [b0, b1]
    
  b0,b1=fit(_input,_output)
    
  def predict(_input):
   	for row in test:
		yhat = b0 + b1 * _input
		predictions.append(yhat)
   	return predictions
    
    
    
