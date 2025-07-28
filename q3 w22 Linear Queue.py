#w22 q3 Queue Linear

global Queue
Queue = [-1]*100 #integer
print(Queue)

headpointer = -1
tailpointer = 0 #next free space 

def Enqueue(DataInput):
    global Queue
    global tailpointer
    global headpointer
    if tailpointer < 100: #check if queue full
        Queue[tailpointer] = DataInput
        tailpointer = tailpointer +1 
        return True
        if headpointer == -1: #head pointer always points towards 1 value 
            headpointer = 0
    else:
        return False
#c            
for i in range(1,21): #1 to 20 inclusive added in queue in ascending order
    res = Enqueue(i)
 
if res  == True :#check if all entered
   print("Successful")
else:
  print("unsuccessful")        
  
print(Queue)  


    
def Dequeue():
    global Queue
    global headpointer
    global tailpointer
    if headpointer == -1: #can be zero
        print("Queue is empty")
    else:
        returnitem = Queue[headpointer]
        print(returnitem)
        headpointer = headpointer + 1 #head pointer increments points to next value 
        
    #reset karna ki condition for queue
    if  headpointer == tailpointer :
        tailpointer  = 0
        headpointer = -1
              
def RecursiveOutput(start):
    if start == headpointer: #0
        return Queue[start]
    else:
        return RecursiveOutput(start -1)+ Queue[start]
    
mysum = RecursiveOutput(tailpointer -1 )    
    
    