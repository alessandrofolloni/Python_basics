def select(a, b, n):
    #your definition here
    if len(a)!=len(b):
        return a
    i=0
    while i in range(len(a)):
        if len(a[i])!=len(b[i]):
            return a 
        i+=1
    
    c=[]
    i=0
    while i in range(len(a)):
        j=0
        while j in range(len(a[i])):
            if b[i][j]<n:
                c.append(a[i][j])
            j+=1
        i+=1
    return c
    
print(select([[0, 4, 3, 7],
              [3, 2, 4, 4],
              [6, 6, 6, 2]], 
             [[1, 2, 9, 5], 
              [2, 9, 6, 7],
              [7, 2, 3, 2]], 
              6))