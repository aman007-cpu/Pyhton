class Employee:
    company = "google"

    def ShowDetails(self):
        print("hello there")

class programmer(Employee):
    lang = "pyhton"
    def getlang(self): 
        print("language is "+ self.lang)

e = Employee()
p = programmer()
e.ShowDetails()
p.ShowDetails()
print(p.company)