class Person:
    country = "india"
    def takeBreath(self):
        print("i am breathing")
    
class Employee(Person):
    company = "infosys"

    def getsalary(self):
        print(f"salary is  {self.company}")
    def takeBreath(self):
        print("i am an employee thats why breathing")
class Programmer(Employee):
    company = "fiver"

    def getsalary(self):
        print("No salary ")    

p = Person()
p.takeBreath()
e = Employee()
pr = Programmer()
