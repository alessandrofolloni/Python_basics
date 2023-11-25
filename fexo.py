#do not insert print, or tests
def fexp(L):
    if len(L)<2:
        return True
    som=L[0]
    i=1
    c=True
    while i in range(1,len(L)):
        if som!=L[i]:
            L[i]=som
            c=False
        som+=L[i]
        i+=1
    if c==False:
        return False
    return True    
    

exec('LL=[1,2,3] \nprint(fexp(LL)) \nprint(LL)')