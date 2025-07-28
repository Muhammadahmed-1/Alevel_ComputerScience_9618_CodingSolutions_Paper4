#s22 qp43 
#q1
#File Data :ARRAY[0:9 , 0:1] OF STRING
FileData = [[""]*2 for x in range(10)]

def ReadHighScore():
    Filename = "HighScore.txt"
    File = open(Filename,'r')
    for x in range(0,10):
        FileData[x][0]= File.readline().strip()
        FileData[x][1]= File.readline().strip()
    File.close()
    
def OutputHighScore():
    for x in range(0,10):
        print(FileData[x][0] + " " + FileData[x][1])


#e ii       
def ArrangePattern(PlayerName,Score):
    if Score > FileData[x][1]:
       Temp1 = FileData[x][0]
       Temp2 = FileData[x][1]
       FileData[x][0] = PlayerName
       FileData[x][1] = Score
       Count = x +1
       while count < 10 :
           Second1 = FileData[Count][0]
           Second2 = FileData[Count][1]
           FileData[Count][0] = Temp1
           FileData[Count][1] = Temp2
           
           Temp1 = Second1
           Temp2 = Second2
           Count = Count +1
           break;
#e iii / d i ii e i
ReadHighScore()
OutputHighScore()

PlayerName = "4characters"
while PlayerName != 3:
    PlayerName = input("Enter 3 chara name")
        
Score = -1 
while Score < 1 or Score> 1000:
    Score = int(input("Input Score")           
                
ArrangePattern(PlayerName,Score)
OutputHighScore()