#S42 MJ 2022 OOP

class Card:
    #PRIVATE DECLARE Number:int
    #PRIVATE DECLARE Number : Colour
    
    def __init__(self,Num,Col):
        self.__Number =Num
        self.__Colour = Col
        
    def GetNumber(self):
        return self.__Number
    
    def GetColour(self):
        return self.__Colour
  
filename = "CardValues.txt"
CardArray = []
try:
      
      file = open(filename , "r")
      for i in range(30):
          
          Num = int(file.readline())
          Col = file.readline()
          CardArray.append(Card(Num,Col)) # CardArray[i] = Card(Num, Col)
      file.close()
except IOError: 
     print ("end of fle")      
     
def ChooseCard():
   global CardArray
   flag = False
   cardindex = 0
   while flag != True: #not flag 
       cardindex = int(input("Input value between 1 to 30 "))
       if cardindex <1 or cardindex > 30 :
           print("Enter the value again")
       else:
           if CardArray[cardindex -1] == "Taken":
               flag  = False
              
           else:
              flag = True
   
   selected_card = CardArray[cardindex-1]           
   CardArray[cardindex - 1] = "Taken"       
   return selected_card

Player1 = []
#pLAYER1 = [] OF CARD

for i in range(4):
    ReturnIndex = ChooseCard()
    Player1.append(CardArray[ReturnIndex])
    
for i in range(4):
   print(Player1[i].GetNumber())
   print(Player1[i].GetColour().strip()) #outputting 4 cards colour