import numpy as np

def checkerboard(n):
    a=np.zeros((n,n),dtype=int)
    a[1::2,::2]=1
    a[::2,1::2]=1
    return a

print(checkerboard(3))