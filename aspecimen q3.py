#specimen q3
QueueData = ["" for i in range(20)]
print(QueueData)

QueueArray = []
for  i in range(20):
    Element = input("Enter the values to be entered: ")
    QueueArray.append(Element)
StartPointer = 0
EndPointer = 0     

def Enqueue(item):
    global EndPointer
    if EndPointer < len(QueueArray):#20
        return False
    else:
        QueueData[EndPointer]= item
        EndPointer =EndPointer  + 1
        return True
        
def ReadFile(QueueData):
    file = input("Enter the file name ")
    try:
        file = open(file,"r")
        Inserted = True
        DataAdd = file.readline().strip()
        while Inserted == True and DataAdd != None:
            Inserted = Enqueue(QueueData)
            DataAdd = file.readline().strip()
        file.close()
        if Inserted == True :
            return 1
        else:
            return 2
    except FileNotFoundError:
    
       return -1
   
x= ReadFile()
if x == -1:
    print("File is not found")
elif x == 2:
    print("Added successfully")
else:
    print("full cannot add")    
    
               
        
           