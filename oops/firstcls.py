class Number:
    def sum(self):
        return self.a +self.b

num = Number()
num.a =9
num.b=8
s = num.sum()
print(s)

class Railway:
    formType = "Railway"
    def printdata(self):
        print(f"name is {self.name}")
        print(f"Train is {self.train}")


obj = Railway()
obj.name = "aman"
obj.train = "Nibu"
obj.printdata()