class HiddenBox:
    #__ BoxName String
    #__ Creater String
    #__ GameLocation String
    #__ DataHidden Date
    #__LastFinds [10] [2] String
    #__Active String
    def __init__(self,BoxNameP,CreatorP,HiddenP,GameLocationP):
        self.__BoxName =BoxNameP
        self.__Creator = CreatorP
        self.__DateHidden = HiddenP
        self.__GameLocation = GameLocationP
        self.__LastFind =  [["" for col in range(0,2)]for i in range(0,10)]
        self.__Active =False 
    def GetBoxName ():
        return self.__BoxName
    def GetLocation():
        return self.__GetLocation
    
    