#s21 mj 42


def linearSearch(item):
    for i in range(0,10):
        if arrayData[i]==item:
            return True
        else:
            return False
        
 
arrayData = [10,5,6,7,1,12,13,15,21,8]       
item = int(input("Enter search item"))
           
found = linearSearch(item)
if found == True :
    print("item found")
else:
    print("not found")
    
def bubblesort():
    for x in range(0,10):
        for y in range(0,9):
            if theArray[y]< theArray[y+1]:
                temp=theArray[y]
                theArray[y]= theArray[y+1]
                theArray[y+1]=theArray[y]
    
           