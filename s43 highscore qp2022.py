# Define FileData as a two-dimensional list with 10 rows and 2 columns
FileData = [[""] * 2 for x in range(10)]

# Read high scores from a text file and store them in FileData
def ReadHighScore():
    Filename = "HighScore.txt"
    File = open(Filename, 'r')
    for x in range(0, 10):
        FileData[x][0] = File.readline().strip()
        FileData[x][1] = File.readline().strip()
    File.close()

# Output high scores stored in FileData
def OutputHighScore():
    for x in range(0, 10):
        print(FileData[x][0] + " " + FileData[x][1])

# Arrange new high score in the correct position in FileData
def ArrangePattern(PlayerName, Score):
    for x in range(0, 10):
        if Score > int(FileData[x][1]):
            Temp1 = FileData[x][0]
            Temp2 = FileData[x][1]
            FileData[x][0] = PlayerName
            FileData[x][1] = str(Score)
            Count = x + 1
            while Count < 10:
                Second1 = FileData[Count][0]
                Second2 = FileData[Count][1]
                FileData[Count][0] = Temp1
                FileData[Count][1] = Temp2
                Temp1 = Second1
                Temp2 = Second2
                Count =Count +1
            break

# Read high scores from file and output them to the console
ReadHighScore()
OutputHighScore()

# Prompt the user to enter a player name (3 characters)
PlayerName = " "
while len(PlayerName) != 3:
    PlayerName = input("Enter a 3-character player name: ")

# Prompt the user to enter a score between 1 and 1000
Score = -1
while Score < 1 or Score > 10000:
    Score = int(input("Enter a score between 1 and 1000: "))

# Arrange the new high score and output the updated high scores to the console
ArrangePattern(PlayerName, Score)
OutputHighScore() 

def WriteTopTen():
    Filename = "NewHighScore.txt"
    Filenew= open(Filename, 'w')
    for x in range(0,10):
        Filenew.write(str(FileData[x][0])+ '\n')
        Filenew.write(str(FileData[x][1])+ '\n')
        close.Filenew
    