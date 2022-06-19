from Child import sanSiro
from Parent import Stadium,car,aircraft

# Inheritance example
obj1 = sanSiro()
# accessing pitchType method that does not exist in sanSiro class
obj1.pitchType()

# Encapsulation example
obj2 = Stadium()
# putting Basketball value in __sportType
obj2.__sportType = "Basketball"
obj2.stadiumType()

# Polymorphism example
def canFly(test):
    test.fly()

carTest = car()
aircraftTest = aircraft()

# testing polymorphism
canFly(carTest)
canFly(aircraftTest)
