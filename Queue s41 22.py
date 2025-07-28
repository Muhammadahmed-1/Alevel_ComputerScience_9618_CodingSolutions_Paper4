#9618_s41_22
#q3


def Enqueue(addData):
    global tailpointer
    global NumberofItems
    if NumberofItems>= 10:
        return False
    QueueArray[tailpointer] = addData
    if tailpointer >= 9:
        tailpointer = 0
    else:
        tailpointer=tailpointer+1
    NumberofItems=NumberofItems +1
    return True
    
def Dequeue():
    global headpointer
    global NumberofItems
    if NumberofItems == 0 :
        return False
    else:
        ReturnItem = QueueArray[headpointer]
        QueueArray[headpointer]= ""
        if headpointer < Queuefull -1:
            headpointer = headpointer+1
        else:
            headpointer = 0
        NumberofItems =NumberofItems -1
        return ReturnItem
                   
QueueArray=[]
empty = ""
upperlimit = 10
for i in range(upperlimit):
    QueueArray.append(empty)
print(QueueArray)

headpointer= 0
tailpointer =0
Queuefull = len(QueueArray)
NumberofItems = 0

for i in range(0,11):
    addData= str(input("Enter data"))
    works = Enqueue(addData)

    if works == True:
        print("data enqeued success")
    else:
        print("full")

for i in range(0,2):
    Results = Dequeue()
    if Results != False:
        print(Results)

