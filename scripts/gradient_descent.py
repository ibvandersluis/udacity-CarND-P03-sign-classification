#!/usr/bin/enb python3

import numpy as np

def sigmoid(x):
    """
    Calculate sigmoid
    """
    return 1/(1+np.exp(-x))
    
def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))

learnrate = 0.5
x = np.array([1, 2])
y = np.array(0.5)

# Initial weights
w = np.array([0.5, -0.5])

# Calculate one gradient descent step for each weight
nn_output = sigmoid(x[0]*w[0] + x[1]*w[1])

error = y - nn_output
error_term = error * sigmoid_prime(np.dot(x,w))

del_w = [ learnrate * error_term * x[0],
                 learnrate * error_term * x[1]]

print('Neural Network output:')
print(nn_output)
print('Amount of Error:')
print(error)
print('Change in Weights:')
print(del_w)