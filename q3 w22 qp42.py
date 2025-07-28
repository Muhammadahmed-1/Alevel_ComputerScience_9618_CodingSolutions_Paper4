#w22 qp42
global Queue

Queue =[]
for i in range(100):
    Queue.append(-1)
HeadPointer =-1 
TailPointer = 0
NumInQueue = 0

def enqueue(AddInteger):
    global  TailPointer
    global  HeadPointer
    if (TailPointer < 100) :
        Queue[TailPointer] = AddInteger
        TailPointer = TailPointer +1 
        return True
        if HeadPointer == -1:
            HeadPointer= 0
    else:
        return False
    
Success = False
for Count in range(0,20):
    Success = enqueue(Count)
if Success == False:
   print("unSuuccessfully ")    
else: 
    print("success")
    
def RecursiveOutput(Start):
    if (Start==0):
            return Queue[Start]
    else:
        return Queue[Start]+ RecursiveOutput(Start -1 )
    
print(str(RecursiveOutput(TailPointer -1 )))   