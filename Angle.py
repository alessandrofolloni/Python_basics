class Angle:
    __size=None
    
    def __init__(self,m=0):
        self.__size=m
    
    def adjust(self):
        if self.__size<0:
            while self.__size<0: self.__size+=360
        if self.__size>=360:
            while self.__size>=360: self.__size-=360

    def __str__(self):
        return str(self.__size)+'°'
        
    def get(self):
        self.adjust()
        return self.__size
    
    def __add__(self,a):
        res=Angle()
        res.__size=self.__size+a.__size
        res.adjust()
        return str(res)
    
    def __sub__(self,a):
        res=Angle()
        res.__size=self.__size-a.__size
        res.adjust()
        return str(res)
    
    def __mul__(self,p):
        res=Angle()
        res.__size=self.__size*p
        res.adjust()
        return str(res)
        
    def __floordiv__(self,d):
        res=Angle()
        res.__size=self.__size//d
        res.adjust()
        return str(res)
    
print(Angle(500).get())