class A:
    def __init__(self, xx): 
        self.__x = xx
    def get(self): 
        return self.__x
class B(A):
    pass

class C(B):
    def get(self):
        #INSERT HERE THE BODY OF get
        return super().get()
        
    def __add__(self,other):
        return C(self.get()+other.get())
    
    #INSERT YOUR OTHER METHOD DEFINITIONS, if needed
    def __str__(self):
        return 'C: '+ str(self.get())

#DO NOT MODIFY FROM HERE!
b=C(10)
c=C(20)
print(b+c)
b=C(70)
c=C(7)
print(b+c)