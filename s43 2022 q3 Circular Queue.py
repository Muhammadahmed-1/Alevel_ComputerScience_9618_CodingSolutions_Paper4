#s43 2022 q3 Circular Queue
QueueArray = [""] * 10
headpointer = 0
tailpointer = 0
numofitems = 0
#can not pass them as Byreference so declared them as global variables
def Enqueue(DatatoAdd):
    global QueueArray
    global headpointer
    global tailpointer
    global numofitems
    if numofitems == 10 :
        return False
    QueueArray[tailpointer] = DatatoAdd
    if tailpointer >= 9:
        tailpointer = 0
    else:
        tailpointer = tailpointer + 1
    numofitems = numofitems + 1
    return True
#can not pass them as Byreference so declared them as global variables
def Dequeue():
    global QueueArray
    global headpointer
    global tailpointer
    global numofitems
    if numofitems == 0:
        return False
    else:
        returnitem = QueueArray[headpointer]
        headpointer = headpointer + 1
        if headpointer >=9: #queueful -1 
           headpointer = 0
           
        numofitems = numofitems -1
        return returnitem
            
     
for i in range(1,12):
    DatatoAdd = str(input("Enter the data to be added "))
    res = Enqueue(DatatoAdd)
    if res == True:
        print("success")
    else:
        print("not added")

for i in range(0,2):
    result = Dequeue()
    if result != False:
        print( "Output value is : "+ result )
        

        
    
    

