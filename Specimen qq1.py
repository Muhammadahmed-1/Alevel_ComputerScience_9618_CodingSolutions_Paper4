#Specimen q1

global TheData            
TheData = [20,3,4,8,12,99,4,26,4]

def InsertionSort(TheData):
    for Count in range(0,len(TheData)):
        DataToInsert = TheData[Count]
        Inserted= 0
        NextValue = Count -1
        while (NextValue>=0)and Inserted != 1:
            if (DataToInsert < TheData[NextValue]):
                TheData[NextValue+1]= TheData[NextValue]
                NextValue=NextValue-1
                TheData[NextValue+1]=DataToInsert
            else:
                Inserted=1

def displayarray(TheData):
    for i in range(0,len(TheData)):
        print(TheData[i])
    
def search(TheData):
    item= int(input("Enter search item"))
    for i in range(0,len(TheData)):
        if TheData[i]==item:
            print('found')
            return True
    print("Not found")
    return False
    
print("before sort")
displayarray(TheData)

print("aFTER SORT")
InsertionSort(TheData)
displayarray(TheData)             
Search(TheData)

for i in range(0,2):
    res = search(TheData)