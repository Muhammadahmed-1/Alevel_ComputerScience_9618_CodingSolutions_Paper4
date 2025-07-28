ArrayNodes = []
for i in range(0,20):
    ArrayNodes.append([0,0,0])
    
ArrayNodes = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1],[-1,-1,-1]]
FreeNode = 6
RootPointer = 0

def SearchValue(RootPointer,ValueToFind):
        
    if RootPointer == -1 :
        return -1
    else:
        if ArrayNodes[RootPointer][1] ==ValueToFind:
            return RootPointer
        else:
            if ArrayNodes[RootPointer][1] == -1:
                return -1
    if ArrayNodes[RootPointer][1] > ValueToFind:
        return SearchValue(ArrayNodes[RootPointer][0] , ValueToFind)
    
    if ArrayNodes[RootPointer][1] < ValueToFind:
        return SearchValue(ArrayNodes[RootPointer][2], ValueToFind)
                           
#d 
def PostOrder(RootNode):
    if RootNode[0] !=-1 :
        PostOrder(ArrayNodes[RootNode[0]])
    if RootNode[2] != -1 :
        PostOrder(ArrayNodes[RootNode[2]])
    print(str(RootNode[1]))

ReturnVal = SearchValue(RootPointer, 15)
if ReturnVal == -1 :
    print("Not FOUND")
else:
    print("Found" + str(ReturnVal))

PostOrder(ArrayNodes[RootPointer])
    #basically ArrayNodes[RootPointer] is RootNode
    