class A:
    def __init__(self, xxx):
        self.x=xxx
    def foo(self,e):
        return self+e

class B(A):
    #complete this definition
    #method foo CANNOT be overridden (redefined)
    def __add__(self,other):
        return self.x**other.x
    
       

print(B(10).foo(B(2)))