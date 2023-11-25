import numpy as np

def exchangecolumns(a):
    if a.shape[1]%2!=0:
        return None
    perm=np.arange(0,a.shape[1])
    perm+=(-1)**(perm%2)
    return a[:,perm]

print(exchangecolumns(np.arange(0,20).reshape(5,4)))