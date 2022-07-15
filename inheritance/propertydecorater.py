class Employee:
    company = "NON0"
    salary = 3240
    salarybonus = 788
    @property
    def total(self):
        return self.salary + self.salarybonus
    @total.setter
    def total(self,val):
        self.salarybonus = val - self.salary
        
e = Employee()
print(e.total)
e.total = 5000
print(e.salary)
print(e.salarybonus)