class Animal:
    animal = "mammal"
class Pet(Animal):
    color = "white"
class Dog(Pet):
    @staticmethod
    def bark():
        print("bhao bhao")

d = Dog()
d.bark()
