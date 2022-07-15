class Person:
    def __init__(self):
        print("initializing.....\n")
    country = "india"
    def takeBreath(self):
        print("i am breathing")
    
class Employee(Person):
    def __init__(self):
        super().__init__()
        print("Employee initializing.....\n")
    company = "infosys"

    def getsalary(self):
        print(f"salary is  {self.company}")
    def takeBreath(self):
        super().takeBreath()
        print("i am an employee thats why breathing")
class Programmer(Employee):
    company = "fiver"

    def getsalary(self):
        print("No salary ")  
    def takeBreath(self):
        super().takeBreath()
        print("i am Programmer thats why ++()breathing")      

p = Person()
# p.takeBreath()
e = Employee()
# e.takeBreath()
# pr = Programmer()
# pr.takeBreath()
