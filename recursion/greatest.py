def great(a,b,c):
    if(a>b):
        if(a>c):
            return a
        elif(a<c):
            return c
    elif(b>c):
        return b
    else:
        return c            


m = great(6,2,7)
print(m)

print("hello",end=" ")
print("dsds",end=" ")