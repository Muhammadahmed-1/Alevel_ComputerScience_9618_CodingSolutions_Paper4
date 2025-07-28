
class TreasureChest :
    #PRIVATE question:STRING
    #PRIVATE answer:INTEGER
    #PRIVATE points :INTEGER
    
    def __init__(self,questionP,answerP,pointsP):
        self.__question=questionP
        self.__answer= questionP
        self.__points=pointsP
    # update the method name to follow Python convention
    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answer):
        if answer == self.__answer:
            return True
        else:
            return False

    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points // 2)
        elif attempts == 3 or attempts == 4:
            return int(self.__points // 4)
        else:
            return 0


# create an empty list to hold TreasureChest objects
arrayTreasure = []

# define the readData function to populate the arrayTreasure list
def readData():
    global arrayTreasure
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, "r")
        dataFetched = file.readline().strip()
        while dataFetched != "":
            question = dataFetched
            answer = int(file.readline().strip())  # cast answer to int
            points = int(file.readline().strip())  # cast points to int
            # create a new TreasureChest object and add it to the arrayTreasure list
            chest = TreasureChest()
            chest.setQuestionAnswerPoints(question, answer, points)
            arrayTreasure.append(chest)
            dataFetched = file.readline().strip()
        file.close()  # close the file when finished
    except IOError:
        print("File not found")

# call the readData function to populate the arrayTreasure list
readData()

# get user input for which question to ask
choice = int(input("Enter a number between 1 and 5: "))
if choice > 0 and choice < 6:
    result = False
    attempts = 0
    while result == False:
        answer = int(input(arrayTreasure[choice - 1].getQuestion() + ": "))  # prompt user for input
        result = arrayTreasure[choice - 1].checkAnswer(answer)
        attempts += 1
    print(arrayTreasure[choice - 1].getPoints(attempts))  # print the number of points earned
