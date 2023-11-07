# M03_Case_Study_Car_classes.py
# Mark Atkins  11/07/2023
"""
Python app that has the following classes:
A super class called Vehicle, which contains an attribute for vehicle type, such as car, truck, plane, boat, or a broomstick.
A class called Automobile which will inherit the attributes from Vehicle and also contain the following attributes:
 year
 make
  model
 doors (2 or 4)
 roof (solid or sun roof).

The app accepts user input for a car. The app stores "car" into the vehicle type in your Vehicle super class. 
The app  asks the user for the year, make, model, doors, and type of roof and stores thde data in the attributes above.
The app outputs the data in an easy-to-read and understandable format, Ex:
  Vehicle type: car
  Year: 2022
  Make: Toyota
  Model: Corolla
  Number of doors: 4
  Type of roof: sun roof
"""

class Vehicle:
    def __init__(self, vehicle_type ='car'):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type ='car', year ='0', make ='unknown', model ='unknown', doors=3, roof ='unknown'):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display(self):  ## print out the car values
        print(f"\nVehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

#  Test the classes, as described above:
year = input("Enter the year of manufacture: ")
make = input("The make of the vehicle: ")
model = input("The model: ")
doors = input("The number of doors (2 or 4): ")
roof = input("The type of roof (solid or sun roof): ")

car1 = Automobile('car', year, make, model, doors, roof)
car1.display()

print("\n============== Testing a truncated call to constructor for default attribute values: =============")
car2 = Automobile()
car2.display()

