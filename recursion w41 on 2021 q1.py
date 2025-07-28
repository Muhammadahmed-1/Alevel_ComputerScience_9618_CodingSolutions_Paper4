#recursion w41 on 2021 q1
def Unknown(X,Y):
    if X < Y:
        print(X+Y)
        return (Unknown(X+1, Y)*2)
    else:
        if X ==Y :
            return 1
        else:
            print(X+Y)
            return (Unknown(X-1, Y)// 2)

print("10 and 15")
x = Unknown(10, 15)
print(x)

y = Unknown(10, 10)
print(str(y))

def iterativeUnknown(X,Y):
    Total = 1
    while X != Y:
        print(str(X+Y))
        if X < Y :
            X = X + 1
            Total = Total *2
        else:
            X = X - 1
            Total = Total // 2
    return Total        
            
            
print("10 and 15")
print(str(iterativeUnknown(10, 15)))
print("10 and 10")
print(str(iterativeUnknown(10, 10)))       
            
    