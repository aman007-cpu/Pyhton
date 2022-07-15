class Vector:
    def __init__(self,vec):
        self.vec = vec
    def __str__(self):
        str1=""
        index=0
        for i in self.vec:
            str+=f"{i}a{index} +"
            index +=1
        return str1[:-1]
        
v = Vector([1,2,3,4]) 
print(v)           
            