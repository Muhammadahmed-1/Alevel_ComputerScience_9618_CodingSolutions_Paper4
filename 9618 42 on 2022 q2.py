#9618 42 on 2022 q2 

class Character:
    #PRIVATE DECLARE Name : STRING
    
    
    def __init__(self,NameP,XCoordinateP, YCoordinateP):
        self.__Name = NameP
        self.__XCoordinate = XCoordinateP
        self.__YCoordinate = YCoordinateP
        
    def GetName(self):
        return self.__Name
    def GetX(self):
        return self.__XCoordinate
    
    def GetY(self):
        return self.__YCoordinate
    
    def ChangePosition(self,XChange,YChange):
        self.__XCoordinate = self.__XCoordinate + XChange
        self.__YCoordinate = self.__YCoordinate + YChange
        
CharactersArray = [Character("", 0, 0)]*10
#DECLARE CharactersArray :ARRAY[0:10] OF Character


filename = "Characters.txt" 
try:
    file = open(filename ,"r")
    for Count in range(0,10):
        Name = file.readline().strip().lower()
        XCoordinate = int(file.readline().strip())
        YCoordinate = int(file.readline().strip())
        CharactersArray[Count] = Character(Name, XCoordinate, YCoordinate)
        Name = file.readline().strip()
        #XCoordinate = int(file.readline().strip())
        #YCoordinate = int(file.readline().strip())
        #CharactersArray.append(Character(Name, XCoordinate, YCoordinate))
    
       
    file.close()    
except IOError:
    print("file not found")
Flag = False
Count = 0
while not Flag:
    
    CharacterName = input("Enter the charactername ").lower()
    for i in range(0,10):
        if CharactersArray[i].GetName() == CharacterName:
            
            Count = i -1
            Flag = True 
            break
              
Valid = False
while not Valid:
      letter = input("Enter letter a, w, s or D").upper()
      if letter =='A':
          CharactersArray[Count].ChangePosition(-1,0)
          Valid = True
      elif letter == 'W' :
          CharactersArray[Count].ChangePosition(0,+1)
          Valid =True
      elif letter == 'S':
          Valid = True
          CharactersArray[Count].ChangePosition(0, -1)
      elif letter == 'D':
          Valid = True
          CharactersArray[Count].ChangePosition(+1, 0)          
      #or letter== 'W' or letter== 'S' or letter== 'D':
      else:
         Valid = False
CharacterName = CharactersArray[i].GetName()
X= CharactersArray[i].GetX()         
Y= CharactersArray[i].GetY()

print(CharacterName + ""+ "has changed coordinates to X = " + str(X) + str(Y))


                        
            