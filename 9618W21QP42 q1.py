#9618/W21/QP/42
#1a

def Unknown(X,Y):
    if X < Y:
        print(X+Y)
        return Unknown(X+1, Y)*2
    else:
        if X == Y :
            return 1
        else:
            print(X+Y)
            return(Unknown(X-1, Y)// 2)
#b
print("10 and 15")
X= Unknown(10,15)
print("ReturnValue is ",str(X))

#c
def IterativeUnknown(X,Y):
    Total = 1
    while X != Y:
        print(str(X + Y))
        if X < Y :
            X=X+1
            Total = Total *2
        else:
            X = X-1
            Total = int(Total/2)
    return Total        
    
#di
print("10 and 15")
print(str( IterativeUnknown(10, 15))) 
print("10 and 10")
print(str( IterativeUnknown(10, 10)))
print("15 and 10")
print(str( IterativeUnknown(15, 10)))      