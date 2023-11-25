import numpy as np

def zerocolumns(a):
    c=a.prod(axis=0)!=0
    return a[:,c]

print(zerocolumns(np.array([[1,2,0],[3,1,1],[3,3,0]])))