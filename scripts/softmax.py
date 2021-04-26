#!/usr/bin/env python3

import numpy as np

# Input L is a list of values. Return is a list of softmax values for that list
def softmax(L):
    results = []
    for n in L:
        denom = 0.0
        for score in L:
            denom += np.exp(score)
        results.append(np.exp(n)/denom)
    return results

# A shorter alternative provided by udacity
def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)