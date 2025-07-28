class Balloon:
    #PRIVATE DECLARE Health : INTEGER   
    #PRIVATE
    def __init__(self,DefenceItemP,ColourP,):
        self.__DefenceItem = DefenceItemP
        self.__Colour = ColourP
        self.__Health = 100
        
    def GetDefenceItem(self):
        return self.__DefenceItem
    
    def ChangeHealth(self,Val):
        self.__Health = self.__Health + Val
        
    def CheckHealth(self):
        if self.__Health <= 0:
            return True
        else:
            return False
        
DefenceItem = input("Enter defence item")
Colour = input("Enter colour")
Balloon1 = Balloon(DefenceItem,Colour)

def Defend(BalloonObj):
     Strength = int(input("Enter strength"))
     BalloonObj.ChangeHealth(-Strength)
     print(BalloonObj.GetDefenceItem())
     res = BalloonObj.CheckHealth()
     if res == True:
         print("No health")
     else:
         print("some health remains")
     return BalloonObj    
         
Balloon1 = Defend(Balloon1)     
             
        