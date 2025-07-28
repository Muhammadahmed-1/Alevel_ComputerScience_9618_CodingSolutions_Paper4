#s42 qp 22
#Q2

import random
ArrayData = [[0]*10 for i in range(10)]
for x in range(0,10):
    for y  in range(0,10):
        ArrayData[x][y] = random.randint(1, 100)
        
        
        
def display(ArrayData):
    for x in range(0,10):
        for y in range(0,10):
            print(ArrayData[x][y]," ", end ='')    
            print("")
print("Before")
display(ArrayData)        


    
arrayLength = 10
for x in range(arrayLength):
    for y in range(arrayLength - 1):
        for z in range(arrayLength - y - 1):
            if ArrayData[x][z] > ArrayData[x][z+1]:
                temp = ArrayData[x][z]
                ArrayData[x][z] = ArrayData[x][z+1]
                ArrayData[x][z+1] = temp
                

print("After")
display(ArrayData)                

""""ArrayLength = 10
for X in range(0, ArrayLength-1):
   for Y in range(0, ArrayLength-y-2):
      for Z in range(0, ArrayLength - Y - 2):
         if(ArrayData[X][Z] > ArrayData[X][Z+1]):
             TempNumber = ArrayData[X][Z]
             ArrayData[X][Z] = ArrayData[X][Z+1]
             ArrayData[X][Z+1] = TempNumber  """'
