#w22 qp41 q2
class Card:
    #DECLARE Num : INTEGER
    #DECLARE Colour : STRING
    def __init__(self,NumberP,ColourP):
       self.__Number = NumberP
       self.__Colour = ColourP
       
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
    
    
    
#this for declare cards as a variable of type Card in the main program
#for instance if they ask us take inputs like : 
        #userNum = input("Enter num")
        #usercolor = input("Enter color")
        #card1= Card(usernum,usercolor)
red1 = Card(1, "red")    
red2 = Card(2, "red")   
red3 = Card(3, "red")   
red4 = Card(4, "red")   
red5= Card(5, "red")       

Blue1 = Card(1, "blue")
Blue2 = Card(2, "blue")
Blue3 = Card(3, "blue")
Blue4 = Card(4, "blue")
Blue5 = Card(5, "blue")
    
Yellow1 = Card(1,"yellow")
Yellow2= Card(2,"yellow")
Yellow3 = Card(3,"yellow")
Yellow4 = Card(4,"yellow")
Yellow5 = Card(5,"yellow")


class Hand:
    #DECLARE Cards: ARRAY[0:9] OF Card
    #PRIVATE DECLARE FirstCard : INTEGER
    
    def __init__(self,C1,C2,C3,C4,C5):
        self.__Cards = []
        self.__Cards.append(C1)
        self.__Cards.append(C2)
        self.__Cards.append(C3)
        self.__Cards.append(C4)
        self.__Cards.append(C5)
        self.__FirstCard = 0
        self.__NumberCards = 5
#b i         
    def GetCard(self,index):
        return self.__Cards[index]
Player1 = Hand(red1, red2, red3, red4, Yellow5)  
Player2 = Hand(Yellow2, Yellow3, Yellow4, Yellow5, Blue1)
#c
def CalculateValue(Player):
    Score = 0
    for i in range(0, 4):
        cardHold = Player.GetCard(i)
        Score = Score + cardHold.GetNumber()
        Col = cardHold.GetColour()
        
        if Col == "red":
            Score = Score + 5
        elif Col == "blue":
            Score =Score + 10
        else:
            
            Score =Score +15
        return Score
ScoreP1 = CalculateValue(Player1)
ScoreP2 = CalculateValue(Player2)

if ScoreP2>ScoreP1 :
    print("p2 wins")
elif ScoreP2< ScoreP1:
    print("p1 wins")
else:
    print("DRAW")

    
            
        
        
        