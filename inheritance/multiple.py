class Employee:
    company = "google"

    def ShowDetails(self):
        print("hello there")        

class programmer:
    lang = "pyhton"
    def getlang(self): 
        print("language is "+ self.lang)
class User(programmer,Employee):
    coll = "mait"
    def getcoll(self):
        print(self.getcoll)        

e = Employee()
p = programmer()
u = User()
e.ShowDetails()
u.ShowDetails()
print(u.company)
print(u.lang)