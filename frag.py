P=(2,5)
L=[]
#a SINGLE command here
A,B=list(P)

def g(X):
    for i in range(B):
        X.append(i*A)
        
#a SINGLE command here
g(L)

print(L)