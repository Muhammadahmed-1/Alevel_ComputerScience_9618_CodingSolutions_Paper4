class TreasureChest:
    # PRIVATE question:STRING
    # PRIVATE answer:INTEGER
    # PRIVATE points :INTEGER

    def __init__(self, questionP, answerP, pointsP):
        self.__question = questionP
        self.__answer = answerP
        self.__points = pointsP

def readData():
    global arrayTreasure
    Filename = "TreasureChestData.txt"
    try:
        file = open(Filename, "r")
        dataFetched = (file.readline()).strip()
        while dataFetched != "":
            question = dataFetched
            answer = (file.readline()).strip()
            points = int((file.readline()).strip())
            arrayTreasure.append(TreasureChest(question, answer, points))
            dataFetched = (file.readline()).strip()
        file.close()
    except IOError:
        print("File not found")
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
arrayTreasure = []
readData()
choice = int(input("Enter a number between 1 and 5: "))
if choice > 0 and choice < 6:
    result = False
    attempts = 0
    while result == False:
        answer = input(arrayTreasure[choice - 1].getQuestion())
        result = arrayTreasure[choice - 1].checkAnswer(answer)
        attempts += 1
    print(arrayTreasure[choice - 1].getPoints(attempts))
 