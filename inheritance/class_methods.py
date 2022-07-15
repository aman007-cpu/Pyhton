class Employee:
    company="camel"
    salary = 100
    location = "Delhi"
    # def changesalary(self,sal):
    #     self.__class__.salary = sal
    @classmethod
    def changesalary(cls,sal):
        cls.salary = sal


e = Employee()
print(e.salary)
e.changesalary(455)
print(e.salary)
print(Employee.salary)