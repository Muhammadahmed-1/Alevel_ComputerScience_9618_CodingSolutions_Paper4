#w22 q42 q2
global Jobs
Jobs = [ ]
#Jobs=[0 * 2 for i in range(0,99)]
global NumberOfJobs

def Initailse():
    global Jobs
    global NumberofJobs
    for x in range(0,100):
        Jobs.append([-1,-1])
    NumberofJobs = 0    
    
def AddJob(JobNum ,Priority):
    if NumberofJobs == 100:
        print("Not Added")
    else:
        Jobs[NumberofJobs] = [JobNum,Priority]
        print("Added")
        JobNum = JobNum +1 
Initailse()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)  
AddJob(12, 9)  
AddJob(78, 1)            
        
def InsertionSort():
    global Jobs
    global NumberOfJobs
    
    for i in range (1,NumberOfJobs):
        Current1 = Jobs[i][0]
        Current2 = Jobs[i][1]
        while i > 0 and Jobs[i-1][1]> Current2:
            Jobs[i][0]=Jobs[i-1][0]
            Jobs[i][1]= Jobs[i-1][1]
            i = i -1 
       Jobs[i][0] = Current1
       Jobs[i][1] = Current2
       
def PrintArray():
   for x in range(0,NumOfJobs):
       print(str(Jobs[i][0], , , 
                 )
       