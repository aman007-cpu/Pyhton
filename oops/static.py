class Employee:
    company = "Google"
    def getsalary(self):
        print("Salary is : ",self.salary )
    @staticmethod    
    def greet():
        print("Good moring")


aman =Employee()
aman.salary = 321332
aman.getsalary()
aman.greet()
