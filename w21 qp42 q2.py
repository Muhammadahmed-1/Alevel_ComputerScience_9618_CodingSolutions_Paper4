#qp41 ON 21 #2
#a
class Picture():
    def __init__(self,DescriptionP,WidthP,HeightP,FrameColourP):
        self.__Description=DescriptionP #STRING
        self.__Width=WidthP #Integer
        self.__Height=HeightP #Integer
        self.__FrameColour=FrameColourP #STRING
    #b    
    def GetDescription(self):
        return self.__Description
    def GetWidth(self):
        return self.__Width
    def GetHeight(self):
        return self.__Height
    def GetColour(self):
        return self.__FrameColour
   #c 
    def SetDescription(self,NewDescriptionP):
        self.__Description =NewDescriptionP
#(d)        
ArrayPic =[]
for i in range(100):
   ArrayPic.append(Picture("", 0, 0, ""))    
#(e)
def ReadData(ArrayPic):
    
    FileName ="Pictures.txt"
    Counter =0
    try:
        file = open(FileName , "r")
        Description = (file.readline()).strip().lower()
        while(Description != ""):
            
            Width = int(file.readline().strip())
            Height = int(file.readline().strip())
            Frame= (file.readline()).strip().lower()
            ArrayPic[Counter] = Picture(Description, Width, Height, Frame)
            Description = (file.readline().strip()).lower()
            Counter = Counter +1
        
        file.close()
    except IOError:
       print("Cound not find file")
    return Counter , ArrayPic    
#f      
NumofPicturesInArray, ArrayPic = ReadData(ArrayPic)  

FrameColour = input("Input FrameColour: ").lower()
MaxHeight = int(input("Enter max heig:"))    
MaxWidth = int(input("Enter max width: "))    

for Z in range(0, NumofPicturesInArray):
    if ArrayPic[Z].GetColour() == FrameColour:
        if ArrayPic[Z].GetHeight() <= MaxHeight:
            if ArrayPic[Z].GetHeight() <= MaxWidth:
                print(ArrayPic[Z].GetDescription(),"",str(ArrayPic[Z].GetWidth()),"" ,str(ArrayPic[Z].GetHeight()))
    
    