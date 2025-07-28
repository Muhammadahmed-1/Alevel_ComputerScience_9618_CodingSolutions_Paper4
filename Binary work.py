
#w21 q3
# Binary Tree

def AddNode():
    global ArrayNodes
    global RootPointer
    global FreeNode

    NodeData = int(input("Enter data: ")) 
    if FreeNode <= 19:  # check if space in array tree is not full
        ArrayNodes[FreeNode][0] = -1  # now storing the data set to null
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1
        if RootPointer == -1: 
            # check if the tree is empty, store at start
            RootPointer = 0  # or RootPointer = FreeNode
        else:
            # find the insertion point
            Placed = False
            CurrentPointer = RootPointer 
            while Placed != True: # not Placed
                if NodeData < ArrayNodes[CurrentPointer][1]:  # move left
                    if ArrayNodes[CurrentPointer][0] == -1:  # check space in the left pointer
                        # adjust the pointer
                        ArrayNodes[CurrentPointer][0] = FreeNode
                        Placed = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][0]
                else:
                    if ArrayNodes[CurrentPointer][2] == -1:
                        ArrayNodes[CurrentPointer][2] = FreeNode
                        Placed = True
                    else:
                        CurrentPointer = ArrayNodes[CurrentPointer][2]  # incrementation
        FreeNode = FreeNode + 1  # Move this line inside the if block
        return ArrayNodes
    else:
        print("Tree Full")

def PrintAll(ArrayNodes):
    for i in range(20):
        print(ArrayNodes[i][0], "", ArrayNodes[i][1], "", ArrayNodes[i][2])

RootPointer = -1
FreeNode = 0
ArrayNodes = [[0 for c in range(3)] for r in range(20)]

# Interactive input
data_count = int(input("Enter the number of data entries: "))
for _ in range(data_count):
    AddNode()

PrintAll(ArrayNodes)
