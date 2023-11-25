#do not insert print
A=[10,-20,30, -1]
B=A

def f():
    A=10
    #commands here (only inside the body of the function)
    #do not use the global command
    i=0
    while i in range(len(B)):
        if B[i]<0:
            del B[i]
            continue
        i+=1
    A=B
    return A 
    
    
    #end of commands for the body of f()

#other possible commands here, outside the def of f()
#you cannot use commands which modify A or its binding


#do not modify from here
f()