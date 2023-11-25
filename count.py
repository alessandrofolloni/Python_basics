import numpy as np

def count_common(a,b):
    #same shape for sure
    return np.sum(a==b)

print(count_common(np.array([[1,3,8],
              [4,5,2],
              [3,2,9]]),np.array([[2,3,7],
              [4,5,9],
              [6,6,6]])))