w43 q3 binary tree 


# Initialize an empty list to hold the nodes
ArrayNodes = []

# Append 20 nodes, each with 3 values initialized to -1
for x in range(0,20):
    ArrayNodes.append([-1,-1,-1])

# Add some values to the nodes
ArrayNodes = [[1,20,5],[2,15,-1],[-1,3,3],[-1,9,4],[-1,10,-1],[-1,58,-1],[-1,-1,-1]]

# Initialize a variable to hold the index of a free node
FreeNode = 6

# Initialize the root pointer to 0
RootPointer = 0

# Define a recursive function to search for a value in the binary tree
def SearchValue(RootPointer,ValueToFind):
    
    # Check if the root node is empty
    if RootPointer == -1:
        return -1
    else:
        # Check if the value in the root node matches the value we're searching for
        if ArrayNodes[RootPointer][1] == ValueToFind:
            return RootPointer
        else:
            # Check if the root node has any children
            if ArrayNodes[RootPointer][1] == -1:
                return -1
            
    # If the value we're searching for is less than the value in the root node, search the left subtree
    if ArrayNodes[RootPointer][1] > ValueToFind:
        return SearchValue(ArrayNodes[RootPointer][0] , ValueToFind)
    
    # If the value we're searching for is greater than the value in the root node, search the right subtree
    if ArrayNodes[RootPointer][1] < ValueToFind:
        return SearchValue(ArrayNodes[RootPointer][2], ValueToFind)
                           
# Define a function to traverse the binary tree in post-order
def PostOrder(RootNode):
    # Check if the left child of the root node exists
    if RootNode[0] != -1:
        # Recursively traverse the left subtree
        PostOrder(ArrayNodes[RootNode[0]])
    # Check if the right child of the root node exists
    if RootNode[2] != -1:
        # Recursively traverse the right subtree
        PostOrder(ArrayNodes[RootNode[2]])
    # Print the value in the root node
    print(str(RootNode[1]))

# Search for the value 15 in the binary tree
ReturnVal = SearchValue(RootPointer, 15)

# If the value is not found, print a message
if ReturnVal == -1:
    print("Not FOUND")
else:
    # If the value is found, print a message with the index of the node
    print("Found" + str(ReturnVal))
