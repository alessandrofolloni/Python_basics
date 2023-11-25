import numpy as np

def zeroones(p,q):
    #p and q >=3
    a=np.zeros((p,q))
    b=np.arange(1,(p-2)*(q-2)+1).reshape((p-2,q-2))
    a[1:-1,1:-1]=b
    return a 

print(zeroones(10,3))