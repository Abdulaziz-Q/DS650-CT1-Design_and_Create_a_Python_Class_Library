from Parent import Stadium

# by adding Stadium class in parentheses of class sanSiro we are applying inheritance
class sanSiro(Stadium):
    def __init__(self):
        print("San Siro Stadium")

    # creating instance method
    def team(self):
        print("AC Milan and Inter Milan")

    # creating class method
    @classmethod
    def capacity(cls):
        print(80018,cls)

    # creating static method
    @staticmethod
    def opened():
        print('September 19, 1926')
