#do not insert print or tests
import numpy as np

def select(a, b, n):
    #BEGIN STUDENT CODE HERE
    if a.size!=b.size:
        return a
    a=np.reshape(a,(a.size,))
    b=np.reshape(b,(a.size,))
    c=b<n
    return a[c]
    
    #END STUDEND CODE HERE
    
#DO NOT EDIT BELOW

#test 1
a = np.array([[0, 4, 3, 7],
              [3, 2, 4, 4],
              [6, 6, 6, 2]])
b = np.array([1, 2, 9, 5, 2, 9, 6, 7, 7, 2, 3, 2])

print(select(a, b, 6))

#test 2

a = np.array([[3, 7],
              [1, 3]])

b = np.array([[5, 2],
              [0, 9]])

print(select(a, b, 5))

#test 3
a = np.array([7, 6, 1, 3, 5, 2, 4, 2, 0])

b = np.array([[6, 2],
              [3, 0],
              [3, 5],
              [9, 9],
              [8, 1]])

print(select(a, b, 5))

