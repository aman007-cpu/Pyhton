from mimetypes import init
from re import sub


class Employee:
    company = "Google"
    def __init__(self,name,salary,subuniit):
        self.name = name
        self.salary  = salary
        self.subunit = subuniit
        print("Employee created")
    def getdetails(self):
        print(f"the name of employee is {self.name} and salary is {self.salary} and sub {self.subunit}")
    def getsalary(self):
        print("Salary is : ",self.salary )
    @staticmethod    
    def greet():
        print("Good moring")

aman = Employee("Aman",100,"Printers")    
aman.getdetails()