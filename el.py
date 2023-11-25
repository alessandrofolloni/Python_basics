import numpy as np

def element(a, p):
    try:
        return a.ravel()[p]
    except IndexError:
        return -1

print(element(np.array([[[4,3,6],[3,2,8]],[[1,5,7],[2,6,7]],[[3,6,7],[3,7,4]],[[4,2,7],[4,3,1]],[[5,3,5],[3,6,5]]]), 0))