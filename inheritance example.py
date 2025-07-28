
#inheritance example 
class Vehicle:
    def __init__(self, num_wheels, color):
        self.num_wheels = num_wheels
        self.color = color

    def accelerate(self):
        print("Vroom vroom!")

class Car(Vehicle):  # Car is a subclass of Vehicle
    def __init__(self, num_wheels, color, num_doors):
        super().__init__(num_wheels, color)  # Call the parent class's __init__ method to set num_wheels and color
        self.num_doors = num_doors

    def honk(self):
        print("Beep beep!")

car = Car(4, "red", 2)
print(car.num_wheels)  # Output: 4
print(car.color)  # Output: red
print(car.num_doors)  # Output: 2

car.accelerate()  # Output: Vroom vroom!
car.honk()  # Output: Beep beep!
