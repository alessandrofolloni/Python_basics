from math import gcd

class Fraction:
    __num=None
    __den=None
    __sign=None
    
    def __init__(self,N,D=1):
        if type(N)==int:
            if N>=0:
                self.__sign='+'
                self.__num=N
            else:
                self.__sign='-'
                self.__num=-N
            
        if type(D)==int:
            if D>0:
                self.__den=D
        else:
            self.__sign=None
            self.__num=None
            
    def get(self):
        return (self.__sign,self.__num,self.__den)
    
    def value(self,d):
        v=float(self.__num/self.__den)
        if self.__sign=='-':
            return float(-1*round(v,d))
        else:
            return round(v,d)
    
    def reduce(self):
        div=gcd(self.__num,self.__den)
        self.__num=int(self.__num/div)
        self.__den=int(self.__den/div)
        return self
    
    def __eq__(self, f):
        if type(f)!=Fraction:
            return 'error'
        F1=self.reduce()
        F2=f.reduce()
        
        if F1.__sign==F2.__sign and F1.__num==F2.__num and F1.__den==F2.__den:
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.__sign)+str(self.__num)+'/'+str(self.__den)
    
    def __add__(self,f):
        if not isinstance(f,Fraction):
            return None
        res=Fraction(1,1)
        
        res.__den=self.__den*f.__den
        
        if self.__sign=='-' and f.__sign=='-':
            res.__num=(-self.__num*f.__den)+(-f.__num*self.__den)
        elif self.__sign=='-' and f.__sign=='+':
            res.__num=(-self.__num*f.__den)+(f.__num*self.__den)
        elif self.__sign=='+' and f.__sign=='-':
            res.__num=(+self.__num*f.__den)+(-f.__num*self.__den)
        else:
            res.__num=(self.__num*f.__den)+(f.__num*self.__den)
        
        if res.__num>=0:
                res.__sign='+'
        else:
                res.__num=-res.__num
                res.__sign='-'
                
        return res.reduce()
        
        
	
print(Fraction(-2,3)+Fraction(13,39))