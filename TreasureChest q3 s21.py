# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 16:44:58 2023

@author: Ahmad
"""

class TreasureChest:
    # PRIVATE question:STRING
    # PRIVATE answer:INTEGER
    # PRIVATE points :INTEGER

    def __init__(self, questionP, answerP, pointsP):
        self.__question = questionP
        self.__answer = answerP
        self.__points = pointsP

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answer):
        if int(answer) == self.__answer:
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
def readData():
    global arrayTreasure
    Filename = "TreasureChestData.txt"
    try: 
        file  = open(Filename , "r")
        for i in range(0,5):
            question = file.readline().strip()
            ans= int(file.readline().strip())
            points = int(file.readline().strip())
            arrayTreasure[i] = TreasureChest(question, ans, points)
        file.close()    
    except IOError:
           print("file not found")        



# initialize an empty list to store TreasureChest objects
arrayTreasure = []

# read data from the file and populate the list
readData()

# get user's choice of treasure chest
choice = int(input("Enter a number between 1 and 5: "))

# check if the choice is valid
if choice > 0 and choice < 6:
    result = False
    attempts = 0
    while result == False:
        answer = input(arrayTreasure[choice - 1].getQuestion())
        result = arrayTreasure[choice - 1].checkAnswer(answer)
        attempts += 1
    print(arrayTreasure[choice - 1].getPoints(attempts))

