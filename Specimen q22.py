class HiddenBox :
    #__ BoxName STRING
    #__ Creater : STRING
    #__ DateHidden : DATE
    #__ GameLocation : STRING
    #__ LastFinds: [10][2] STRING
    #__ Active : BOOLEAN    
    
   def __init__(self,NewBoxName , NewCreator, NewDateHidden , NewGameLocation):
         self.__BoxName = NewBoxName
         self.__Creator = NewCreator
         self.__DateHidden = NewDateHidden
         self.__GameLocation = NewGameLocation
         self.__LastFinds = [["" for col in range(0,2)for row in range(0,10)]]
         self.__Active = False    
        
   def GetBoxName():
       return self.__BoxName
   
   def GetLocation():
   return self.__GameLocation

TheBoxes = [HiddenBox("","","","")for i in range (0,10000)]
NumBoxes = 0 
def NewBox(TheBoxes, NumBoxes):
       BoxName = input("Enter the name of the Box")
       Creator = input("Enter the creator's name")
       DateHidden = input("Enter the date hidden")
       GameLocation = input("Enter the game location") 
       TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
       return(NumBoxes +1)
   
NumBoxes = NewBox(TheBoxes, NumBoxes)
    
class PuzzleBox(HiddenBox):
    #PRIVATE PuzzleText : STRING
    #PRIVATE Solution  : STRING
    
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewGameLocation, NewPuzzleText, NewSolution):
        super().__init__(NewBoxName, NewCreator, NewDateHidden, NewGameLocation)#super used to provide a way to access method
        #and attributes of a superclass from sub class
        
        self.__PuzzleText = NewPuzzleText
        self.__Solution = NewSolution
        
def NewBox(TheBoxes, NumBoxes):
    # Prompt user for box details
    BoxName = input("Enter the name of the Box: ")
    Creator = input("Enter the creator's name: ")
    DateHidden = input("Enter the date hidden: ")
    GameLocation = input("Enter the game location: ")
    
    # Create HiddenBox instance with provided details
    newBox = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    
    # Add new box to TheBoxes list at index NumBoxes
    TheBoxes[NumBoxes] = newBox
    
    # Increment NumBoxes to reflect addition of new box
    NumBoxes += 1
    
    # Return updated NumBoxes
    return NumBoxes

# Create TheBoxes list with 10000 empty HiddenBox objects
TheBoxes = [HiddenBox("", "", "", "") for i in range(10000)]

# Initialize NumBoxes to 0
NumBoxes = 0

# Call NewBox to add new box and update NumBoxes
NumBoxes = NewBox(TheBoxes, NumBoxes)        
        
        
       