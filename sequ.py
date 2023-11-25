#do not insert print, or tests
import numpy as np

a = np.array([
             [ 2,  4,  7,  9],
             [ 1,  5, 34, 17],
             [32, 34, 44, 54],
             [14, 15, 16, 19],
             [23, 24, 26, 25]])

b = np.array([
             [26, 25, 29, 32],
             [11, 19, 43,  1],
             [39, 38, 10, 18],
             [ 2, 16, 31, 27],
             [28, 12, 30, 44]])

c = np.array([
      [26, 43, 30, 22],
      [34, 12, 41, 33],
      [38,  2,  3, 23],
      [19,  0,  1, 16],
      [13, 28, 37, 10]])

d = np.array([
      [17, 43, 11, 24],
      [ 7,  1,  3, 23],
      [12, 22, 40,  0],
      [15, 42, 20,  5],
      [36, 10, 44, 38]])

def erroneus(x):
   #your definition here
   a=np.sum(x,axis=0)%2!=0
   b=np.sum(x,axis=1)%2!=0
   return x[b,a]
    
    
print(erroneus(a))