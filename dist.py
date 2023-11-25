import numpy as np

def dist(i,j):
    return np.sqrt(i**2+j**2)

def arraydistance(p,q):
    return np.fromfunction(dist,(p,q),dtype=float)

print(arraydistance(3,3))