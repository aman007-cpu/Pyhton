a = {2,4,1,4,6,2,1}
a.add(3)
print(a)

#empty set

b= set()
b.add(29)
b.add(0)
b.add((3,1,3,0)) #can add tuple in sets not lists
print(b)
print(len(b))
b.remove(29)
print(b)
print(b.pop())
b.union({4,6})
print(b)