class MyException(Exception): pass 

def f(x): 
    if x < 0: 
        raise MyException 
    if type(x) != int: 
        raise TypeError 
    print (x) 
    
for v in [-3, 2.5, 77]: 
    try : 
        f(v) 
    except MyException: 
        print ("Insert a positive number") 
    except TypeError: 
        print ("Insert an integer")