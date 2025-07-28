#s22 q3 
class card:
    #PRIVATE NUMBER ; INTEGER
    def __init__(self,NumberP,ColourP):
        self.__Number =NumberP
        self.__Colour =ColourP
        
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Number
    
CardArray=[]
for i in range(30):
    CardArray.append(0)   
try:
    File= open("CardValues.txt", 'r')
    for x in range(0,30):
        NumRead = int(File.readline())
        ColourRead = File.readline()
        CardArray[x]= card[NumberRead,ColourRead]
    File.close()
except IOError:
        print("File not found")   
    
def ChososeCard():
    
    flagContinue = True
    while  flagContinue == true :
        CardSelect = int(input("card select 1 to 30"))
        if CardSelect < 1 or CardSelect > 30 :
            
      
        