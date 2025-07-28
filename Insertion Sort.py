
#InsertionSort

#Entering the elements in the array 
array=[]
LB= 0
upperlimit= int(input("Enter the limit of the array :"))
for i in range(upperlimit):
    element = int(input("Enter the elements to be entered:"))
    array.append(element)
print("Array before sorting:")
print(array)

for pointer in range(LB+1,upperlimit):
    itemtoinsert = array[pointer]
    currentitem = pointer
    while (currentitem>0) and  array[currentitem -1 ]> itemtoinsert:
        array[currentitem]= array[currentitem-1]
        currentitem =currentitem -1
        
    array[currentitem]= itemtoinsert
print("Array after sorting:")    
print(array) 