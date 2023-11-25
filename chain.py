from math import sqrt

class Point:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def whoareyou (self):
        return self.x, self.y
    def __str__(self):
        return 'Point'+str(self.whoareyou())
    def distance(self,p):
        dist=float(sqrt((self.x-p.x)**2 +(self.y-p.y)**2))
        return dist

class Chain:
    __L=None
    
    def __init__(self,l):
        self.__L=l
    
    def delete_point(self):
        pd=self.__L[-1]
        del self.__L[-1]
        return pd
    
    def add_point(self,p):
        self.__L.append(p)
        return p
    
    def dist_extremes(self):
        p1=self.__L[0]
        p2=self.__L[-1]
        dist=float(sqrt((p1.x-p2.x)**2 +(p1.y-p2.y)**2))
        return dist
    
    def __len__(self):
        som=0
        for i in range(len(self.__L)-1):
            d=self.__L[i].distance(self.__L[i+1])
            som+=d
        return int(som)
    
print(len(Chain([Point(0,0),Point(0,3),Point(4,0)])))
print(Chain([Point(0,0),Point(0,3),Point(4,0)]).dist_extremes())
print(Chain([Point(0,0),Point(0,3),Point(4,0)]).add_point(Point(0,0)))
print(Chain([Point(0,0),Point(0,3),Point(4,0)]).delete_point())