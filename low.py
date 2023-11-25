import numpy as np

def lowest(a,b):
    a=a[:,np.newaxis]
    return np.lcm(a,b)

print(lowest(np.arange(0,10), np.arange(0,5)))