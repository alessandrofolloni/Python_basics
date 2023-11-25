#do not insert print or tests
import numpy as np

def select(a, b, n):
    #BEGIN STUDENT CODE HERE
    if a.size != b.size:
        return a
    if a.shape != b.shape:
        b=b.reshape(a.shape)
        
    return a[b<n]
    #END STUDEND CODE HERE
    

