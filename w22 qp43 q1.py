#q1 O N QP41 22

global DataArray
DataArray = [0 for i in range(100)]
 

def ReadFile():
    global DataArray
    Filename = "IntegerData.txt"
    try: 
        file = open(Filename, "r")
        for x in range(100):
            DataArray.append(int(file.readline().strip('\n')))
        file.close()
    except IOError:
        print("File not found")
ReadFile()        
print(DataArray)         


def FindValues():
        global DataArray
        SearchNum = int(input("INput num:"))
        if SearchNum >= 1 and SearchNum <= 100:
            count = 0
            for x in range(len(DataArray)):
                 if  DataArray[x]== SearchNum:
                     count = count + 1 
            return count
        else:
            print("Invalid input ")
res = FindValues()    
print(res)  

def Bubblesort():
    global DataArray
    for i in range(len(DataArray)):
        
        for j in range(len(DataArray)-1):
            if DataArray[j]> DataArray[j+1]:
                Temp =DataArray[j]
                DataArray[j]=DataArray[j+1]
                DataArray[j+1] = Temp
                
Bubblesort()
print(DataArray)
                  


                
        