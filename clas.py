class Top:
    def __init__(self,c): #DO NOT modify __init__
        if type(c)!=int:
            raise TypeError
        self.__n=c
    #complete here the def of Top, as needed
    def get(self):
        return self.__n
class A(Top):
    #complete here the def of A, as needed
    def __eq__(self, m):
        return self.get()==m.get()
        
class B(A):
    #complete here the def of B, as needed
    def __eq__(self, m):
        return abs(self.get())==abs(m.get())

# DO NOT MODIFY THE FOLLOWING
a1=A(1)
a2=A(-1)

print(a1==a2)

b1=B(1)
b2=B(-1)

print(b1==b2)