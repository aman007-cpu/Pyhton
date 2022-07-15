from cmath import sqrt
from mimetypes import init


class Calculator:
    def __init__(self,number):
        self.number = number
    def square(self):
        v = pow(self.number,2)
        print(v)
    def squarroot(self):
        k = sqrt(self.number)
        print(k)
    @staticmethod
    def greet():
        print("Hello boya/\/")    

hel = Calculator(6)
hel.square()
hel.squarroot()
hel.greet()
