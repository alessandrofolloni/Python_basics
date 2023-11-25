class Seq:
    def __init__(self,seque):
        self.__s=seque
    #INSERT HERE OTHER METHODS IF YOU SEE FIT
    def get(self):
        return self.__s

def prefs(ss):
    #YOUR SOLUTION HERE
    #do not insert prints; only the return of the function
    s=ss.get()
    if len(s)==0:
        return 0
    last=s[0]
    count=1
    for e in s[1:]:
        if e!=last:
            last=e
            count+=1
    return count
        
    
print(prefs(Seq('sottoolii')))