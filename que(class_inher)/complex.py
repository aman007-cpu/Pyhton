class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self,c):
        return Complex(self.r+c.r ,self.i + c.i)   
    def __str__(self):
        return f"{self.r} + {self.i}i"     
c1 = Complex(1,3)
c2 = Complex(4,2)
print(c1+c2)



        