#LINKED LIST 

class node:
    
    def __init__(self,Data,NextNode):
        self.data = Data
        self.nextnode = NextNode
#DECLARE linkedlist : ARRAY[0:9] OF node        
linkedlist = [node(1, 1) , node(5, 4) , node(6, 7) , node(7, -1) ,node(2,2) , node(0,6) , node(0,8), node(56,3), node(0,9),node(0, -1)]     
startpointer  =0 
emptylist = 5
currentpointer = startpointer
def addNode(currentpointer): #byVALUE currentptr is taken as startptr BYVAL 
    global linkedlist
    global emptylist
    currentpointer =startpointer
    Data = int(input("Enter the data to be added "))
    #check if place in array
    if emptylist < 0 or emptylist > 9: # array full
        return False 
    else:
        freelist = emptylist 
        emptylist = linkedlist[emptylist].nextnode #increment the empty list value 
        #create a new node on data 
        newNode = node(Data, -1) #-1 to initailize 
        linkedlist[emptylist] = newNode
        
        previouspointer  = 0 #find the last node pointer and append new node to it 
        
        while (currentpointer != -1):#when it reaches end of list -1
             previouspointer = currentpointer
             currentpointer = linkedlist[currentpointer].nextnode #increment / calculating last value to found
             
        linkedlist[previouspointer].nextnode = freelist       
        return True    

def deleteNode():
    global linkedlist
    global emptylist
    global startpointer
    
    currentpointer = startpointer
    
    datatoremove = int(input("Enter the data to be deleted"))
    
    previouspointer = 0
    while currentpointer!= -1 and linkedlist[currentpointer].data !=datatoremove :
        previouspointer = currentpointer
        currentpointer = linkedlist[currentpointer].nextnode #incrementing
        
    if currentpointer == -1:
       return False #as the data not found not at last node
    else:
        #update the pointers to remove the node
       if currentpointer ==startpointer :#if at startpointer
           startpointer = linkedlist[startpointer].nextnode
           #increment that start pointer so startpointer changed
       else:
           linkedlist[previouspointer].nextnode = linkedlist[currentpointer].nextnode
     #now store that values
       linkedlist[currentpointer].data = 0 #to show its removed optional
       linkedlist[currentpointer].nextnode = emptylist #make it as empty list
       emptylist = currentpointer 
      
       return True
def outputnode(startpointer):
    global linkedlist
    currentpointer = startpointer
    while currentpointer != -1:
        print(str(linkedlist[currentpointer].data))
        currentpointer = linkedlist[currentpointer].nextnode
        
#searching in a linked list
def finditem(currentpointer,SearchValue):
    while current != -1:
        if linkedlist[currentpointer].data == SearchValue:
            return currentpointer
        else:
            currentpointer = linkedlist[currentpointer].nextnode
    return -1 #if its not present in list    

outputnode(startpointer)
returnval = addNode(currentpointer)
print(str(returnval) + "Input")
outputnode(startpointer)

def OrderedInsertionList(currentpointer):
    global linkedlist
    global emptylist
    global startpointer
    currentpointer = startpointer
    Data= int(input("Enter data"))
    if emptylist < 0 or emptylist > 9 :
        return False
    else:
        freelist =emptylist #3store ita value
        emptylist = linkedlist[emptylist].nextnode
        newNode = node(Data, -1) 
        linkedlist[freelist] = newNode
        
        while  currentpointer != -1 and linkedlist[currentpointer].Data < Data :
            previouspointer = currentpointer
            currentpointer = linkedlist[currentpointer].nextnode
            
        if currentpointer == startpointer: #not less data
            linkedlist[freelist].nextnode = startpointer
            startpointer = freelist
        else:
            linkedlist[freelist].nextnode = linkedlist[previouspointer].nextnode #store freelist node value previous pointer node value
            linkedlist[previouspointer].nextnode = freelist #points towards the freelist 
        return True     
         
        
        