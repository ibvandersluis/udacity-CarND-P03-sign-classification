#!/usr/bin/env python3

import numpy as np

def cross_entropy(Y, P):
    result = 0.0
    for n in range(len(Y)):
        if Y[n] == 1:
            result += np.log(P[n])
        else:
            result += np.log(1 - P[n])
    return -result

# Shorter solution (from Udacity)
# def cross_entropy(Y, P):
#     Y = np.float_(Y)
#     P = np.float_(P)
#     return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))