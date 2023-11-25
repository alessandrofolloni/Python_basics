import numpy as np

def colsum(a):
    even=a[::,::2].sum()
    odd=a[::,1::2].sum()
    return np.array([even,odd])

print(colsum(np.array([[2, 7, 8, 0],
                       [3, 9, 3, 4],
                       [4, 0, 1, 3]])))