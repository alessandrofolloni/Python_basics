from copy import deepcopy
from math import gcd


class Fraction:
    def __init__(self, N, D=1):
        if type(N)==int and type(D)==int and D>0:
            if N < 0: 
                self.__sign = "-"
                N = abs(N)
            else:
                self.__sign = "+"
            self.__num = N   
            self.__den = D 
        else: #in case of erroneus initialization, instantiate everything to None
            self.__sign = None 
            self.__num = None
            self.__den = None

    def get(self):
        return self.__sign, self.__num, self.__den
    
    def value(self,d):
        if self.__sign == '+':
            return round(self.__num/self.__den,d)
        else:
            return round(-self.__num/self.__den,d)

    def reduce(self):
        factor=gcd(self.__num,self.__den)
        if factor>1:
            self.__num=self.__num//factor # int
            self.__den=self.__den//factor # int
        return self

    def __eq__(self, other):
        sc = deepcopy(self)
        oc = deepcopy(other)
        sc.reduce() 
        oc.reduce()
        return sc.__sign==oc.__sign and sc.__num==oc.__num and sc.__den==oc.__den
    
    def __str__(self):
        return self.__sign+str(self.__num)+"/"+str(self.__den)
    
    def __add__(self, other):
        ss, sn, sd = self.__sign, self.__num, self.__den 
        os, on, od = other.__sign, other.__num, other.__den
        if ss == '+' and os == '+':
            num = sn * od + on * sd
        elif ss == '+' and os == '-':
            num = sn * od - on * sd
        elif ss == '-' and os == '+':
            num = on * sd - sn * od
        else:
            num = - sn * od - on * sd
        den = sd * od
        f = Fraction(num, den)
        f.reduce()
        return f


class P(Fraction):
    def __init__(self, favourable, possible):
        super().__init__(favourable, possible)
        
    def __str__(self):
        return str(round(self.value(),2)) + "%"
    
    #add you code here
    def get(self):
        return super().get()[1:]
    
    def value(self, d):
        n,d=self.get()
        return n/d*100
    
    def __mul__(self, other):
        sn, sd = self.get()
        on, od = other.get()
        tmp = P(sn*on, sd*od)
        tmp.reduce()
        return tmp
        