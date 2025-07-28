#Specimen q 3
QueueData = []
for i in range(0,20):
    QueueData.append("")
StartPointer = 0
EndPointer = 0

def Enqueue(AddItem):
    def Enqueue(DataToAdd, QueueData, EndP):
        if(EndP == 20): 
            return False, EndP 
        else: QueueData[EndP] = DataToAdd 
        EndP = EndP + 1 
        return True, EndP     