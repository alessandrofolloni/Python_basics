#do not insert tests, or prints

def expand(L):
    #your code here
    i=0
    while i in range(len(L)):
        if L[i]>0:
            j=0
            while j in range(L[i]):
                L.insert(i+1,0)
                j+=1
            i+=j
        elif L[i]<0:
            del L[i]
            continue
        
        i+=1
    return L
        
print(expand([2,-2,3,0,2]))
    