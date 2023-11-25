#do not insert print, or tests
#Insert your code here
class A(Exception):
    pass

class B(A):
    pass
    
    
    

#DO NOT MODIFY THE FOLLOWING
try:
    raise B(10)
except A as x:
    print(x)
