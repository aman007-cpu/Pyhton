mydict ={"fast":"lmao","aman": "coder","ekdi":"hui hui", 
       "ano":{'ak':'lol'},
      "Marks":[1,2,3],1:2}
print(mydict["ano"]['ak'])

print(mydict.keys())
print(mydict.values())

print(mydict.items())
new = {32:3}
mydict.update(new)
print(mydict)
print(mydict.get("aman"))

hinditrans = {"kutta":"dog", "genda":"bull","saanp":"snake","vastu":"item"}
print("options are :" , hinditrans.keys())
v = input("enter the hindi word:\n")
print("meaning of ur word is: ", hinditrans.get(v))
k ={8,"8"}
print(k)