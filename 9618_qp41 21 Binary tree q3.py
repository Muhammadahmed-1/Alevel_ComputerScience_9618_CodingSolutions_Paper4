#BinaryTree
#q3a#a
ArrayNodes = [[0 for c in range(3)] for r in range(20)]
RootPointer = -1
FreeNode = 0             


def AddNode(ArrayNodes,RootPonter,FreeNode):
    global RootPointer
 
    NodeData =  int(input("Enter the node data"))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0]= -1
        ArrayNodes[FreeNode][1]=NodeData
        ArrayNodes[FreeNode][2]=-1
        if RootPointer == -1 :
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer 
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0]==-1:
                        ArrayNodes[CurrentNode][0]= FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2]=FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode= FreeNode +1
        return ArrayNodes , RootPointer , FreeNode
    else:
       print("Tree is full")
       return None       
                        

#c
def PrintAll(ArrayNodes):
    for X in range(0,20):
        print(str(ArrayNodes[X][0]),"",str(ArrayNodes[X][1]),"", str(ArrayNodes[X][2]))
        
#d 

for x in range(0,10):
    ArrayNodes , RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)  
PrintAll(ArrayNodes)      
           
#e
#left,root,right
def InOrder(ArrayNodes,RootPointer):
    if (ArrayNodes[RootPointer][0] != -1):
         InOrder(ArrayNodes, ArrayNodes[RootPointer][0])
    print(str(ArrayNodes[RootPointer][1]))
    if (ArrayNodes[RootPointer][2] != -1):
        InOrder(ArrayNodes, ArrayNodes[RootPointer][2])
        
InOrder(ArrayNodes, RootPointer)       
         
                
                        
            
            
    