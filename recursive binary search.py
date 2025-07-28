#9608/43/m/j/2021 

#Q1 #b
class vendingMachine():
    #private DECLARE items :ARRAY[0:3] OF foodItem
    #private moneyIn : REAL
    
    def __init__(self,item1,items2,item3,item4):
        self.__items = []
        self.__items.append(item1)
        self.__items.append(items2)
        self.__items.append(item3)
        self.__items.append(item4)
        self.__moneyIn = 0
        
      
machineOne = vendingMachine(chocolate,sweets,sandwich,apple)
