#s21 MJ 2021 q3

class TreasureChest :
    #PRIVATE question:STRING
    #PRIVATE answer:INTEGER
    #PRIVATE points :INTEGER
    
    def __init__(self,questionP,answerP,pointsP):
        self.__question=questionP
        self.__answer= questionP
        self.__points=pointsP
#arrayTreasure(5) as treasureChest     
arrayTreasure = []   
def readData():
    global answer
    global points
    Filename ="TreasureChestData.txt"
    try:
        file= open(Filename,"r")
        dataFetched = (file.readline()).strip()
        while( dataFetched != "" ):
            question = dataFetched
            answer= (file.readline()).strip()
            points = (file.read()).strip()
            arrayTreasure.append(treasureChest(question,answer,points))
            dataFetched = (file.readline()).strip()
    except IOError:
           print("File not found")        
            
#c 
    def getQuestion(self):
        return self.__question

    def checkanswer(self,answer):
         if answer == self.__answer:
             return True 
         else:
             return False
    def getpoints(self,attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2 :
            return int(self.__points // 2)
        elif attempts == 3 or attempts ==4 :
            return int(self.__points// 4)
        else:
         
           return 0
readData()
choice = int(input("enter btwn 1and 5"))        
if choice > 0 and choice < 6:
    
    reult = False
    attempts = 0
    while result == False :
        answer = int(input(arrayTreasure[choice -1].getQuestion()))
        results = arrayTreasure[choice -1].checkanswer(answer)
        attempts = attempts +1 
    print(int(arrayTreasure[choice-1].getpoints(attempts)))
        
        
            
         
            
            