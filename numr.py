import numpy as np

def index_product(rows, columns):
    def product(i,j):
        return i*j
    return np.fromfunction(product, (rows, columns))


def smaller_than_index(a):
    #STUDENT CODE FROM HERE
    c=index_product(a.shape[0],a.shape[1])
    b=a<=c
    return a[b] 
    #END STUDENT CODE
    
print(smaller_than_index(np.array([[1, 2, 0, 3],
       [2, 1, 0, 18],
       [1, 2, 3, 4]])))