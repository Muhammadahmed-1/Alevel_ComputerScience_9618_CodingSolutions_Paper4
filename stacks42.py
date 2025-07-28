#s42 stack
global Stackdata
Stackdata = [0] *10
global StackPointer
StackPointer = 0

def Push(AddData):
    global StackPointer
    global Stackdata
    
    if StackPointer > 9: #len(StackData)-1
        return False
    else:
        Stackdata[StackPointer] = AddData
        StackPointer = StackPointer +1
        return True 


        
def Pop():
    global StackPointer
    global Stackdata
    if StackPointer == 0 :
        return  -1
    else:
        StackPointer = StackPointer -1
        returnitem = Stackdata[StackPointer]
        return returnitem



def OutputAll():
    
    for x in range(10):
        print(Stackdata[x])
    print(StackPointer)
    
for i in range(0,11):
    AddData = int(input("Enter data to push  "))
    res = Push(AddData)
    if res == True:
        print("added")
    else:
        print("unadded")
        
    


for i in range(0,2):
    Pop()

OutputAll()        
