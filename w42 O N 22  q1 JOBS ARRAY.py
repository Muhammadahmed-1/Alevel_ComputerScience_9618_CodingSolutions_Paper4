#w42 O N 22 



def Initailise():
   global Jobs
   global NumberofJobs
   for r in range(100):
       Jobs.append([-1,-1])
   NumberofJobs = 0   
   
def AddJob(JobNum, JobPriority):
    global Jobs
    global NumberofJobs
    if NumberofJobs != 100 :
         Jobs[NumberofJobs] = [JobNum,JobPriority] #number of jobs used as index
         print("Added")
         
         NumberofJobs = NumberofJobs +1
    else:
        print("Not added")
         
    
               
Initailise()
AddJob(12,10)
AddJob(526, 9)
AddJob(33,8)
AddJob(12,9)
AddJob(78, 1)
#2D ARRAY INSERTION
def InsertionSort():
   ArraySize = len(Jobs)
   global NumberofJobs
   global Jobs
   for pointer in range(1,ArraySize): #can be Number of jobs
     CurrentItem1 = Jobs[pointer][0]
     CurrentItem2 = Jobs[pointer][1]
     currentpointer =  pointer
     while (currentpointer> 0) and (Jobs[currentpointer -1][1]> CurrentItem2):
           Jobs[currentpointer][0] = Jobs[currentpointer -1][0]
           Jobs[currentpointer][1]= Jobs[currentpointer-1][1]
           
           currentpointer = currentpointer -1
     Jobs[currentpointer][0] = CurrentItem1
     Jobs[currentpointer][1] = CurrentItem2  
     
def PrintArray():
    global Jobs
    global NumberofJobs
    for r in range(NumberofJobs):
        output = (str(Jobs[r][0]) + " Priority " + str(Jobs[r][1]))
        print(output)


global Jobs 
global NumberofJobs #DECLARE NumberOfJobs : INTEGER
#Jobs = []
#Jobs =[0 *2 for  r in range(100)]
NumberofJobs = 0
Intailise()
InsertionSort()
PrintArray()

def Initailise():
   global Jobs
   global NumberofJobs
   for r in range(100):
       Jobs.append([-1, -1])
   NumberofJobs = 0   

def AddJob(JobNum, JobPriority):
    global Jobs
    global NumberofJobs
    if NumberofJobs != 100:
        Jobs[NumberofJobs] = [JobNum, JobPriority]  # number of jobs used as index
        print("Added")
        NumberofJobs = NumberofJobs + 1
    else:
        print("Not added")

Initailise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)

# 2D ARRAY INSERTION
def InsertionSort():
    ArraySize = len(Jobs)
    global NumberofJobs
    global Jobs
    for pointer in range(1, ArraySize):  # can be Number of jobs
        CurrentItem1 = Jobs[pointer][0]
        CurrentItem2 = Jobs[pointer][1]
        currentpointer = pointer
        while currentpointer > 0 and Jobs[currentpointer - 1][1] > CurrentItem2:
            Jobs[currentpointer][0] = Jobs[currentpointer - 1][0]
            Jobs[currentpointer][1] = Jobs[currentpointer - 1][1]
            currentpointer = currentpointer - 1
        Jobs[currentpointer][0] = CurrentItem1
        Jobs[currentpointer][1] = CurrentItem2

def PrintArray():
    global Jobs
    global NumberofJobs
    for r in range(NumberofJobs):
        output = (str(Jobs[r][0]) + " Priority " + str(Jobs[r][1]))
        print(output)

InsertionSort()
PrintArray()
