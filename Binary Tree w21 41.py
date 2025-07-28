#Binary Tree w21 41

#No option to use BYREF in python use as global
def AddNode():
   global ArrayNodes
   global RootPointer
   global FreeNode
   
   NodeData = int(input("data enter : ")) 
   if FreeNode <= 19: #check if space in array tree not full
      ArrayNodes[FreeNode][0] = -1 #now storing the data set to null
      ArrayNodes[FreeNode][1] = NodeData
      ArrayNodes[FreeNode][2] = -1
      if RootPointer == -1 : 
          #check if tree empty store at start
          RootPointer = 0 #or =FreeNode
      else:  #find the insertion point
        Placed = False
        CurrentPointer = RootPointer 
        while Placed == False:
            if NodeData < ArrayNodes[CurrentPointer][1]: #moveleft
            
                if ArrayNodes[CurrentPointer][0] == -1: #check space in left ptr
                     #ajust the pointer
                    ArrayNodes[CurrentPointer][0] = FreeNode
                    Placed = True
                else:
                    CurrentPointer = ArrayNodes[CurrentPointer][0]
            else:
                if ArrayNodes[CurrentPointer][2] == -1:
                        ArrayNodes[CurrentPointer][2] = FreeNode
                        Placed = True
                else:
                        CurrentPointer = ArrayNodes[CurrentPointer][2] #incrementation
                        
            FreeNode = FreeNode +1
            return ArrayNodes
              
   else:
        print("Tree Full")      


#Searching item in Binary
def FindNode(searchItem):
    CurrentPointer = RootPointer             
        
    while CurrentPointer != -1 and ArrayNodes[CurrentPointer][1] != searchItem :
        if searchItem <  ArrayNodes[CurrentPointer][1]:
           CurrentPointer = ArrayNodes[CurrentPointer][0] #moving to left as its less than
        else:
            CurrentPointer = ArrayNodes[CurrentPointer][2]
            
    print(CurrentPointer)      
RootPointer = -1
FreeNode = 0


ArrayNodes = [[0 for c in range(3)] for r in range(20) ]    
#c printing all elements in ArrayNodes

def PrintAll(ArrayNodes):
    for i in range(0,20):
        print(str(ArrayNodes[i][0]),"",str(ArrayNodes[i][1]) , "" , str(ArrayNodes[i][2]))

for j in range(10):
     AddNode() 

PrintAll(ArrayNodes)    