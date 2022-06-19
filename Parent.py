class Stadium:
    def __init__(self):
        # Encapsulation restricts __sportType variable to prevent data from direct modification
        # by using underscore as prefix __sportType
        self.__sportType= 'Foorball'

    # creating instance method
    def stadiumType(self):
        print("Sport is: {}".format(self.__sportType))

    # creating class method
    @classmethod
    def pitchSize(cls):
        print("105x68",cls)

    # creating static method
    @staticmethod
    def pitchType():
        print('Grass')

# creating two classes for polymorphism example
class car:
    def fly(self):
        print('Cars can not fly')

class aircraft:
    def fly(self):
        print('Aircrafts can fly')