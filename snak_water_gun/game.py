import random

def game(comp,you):
    if comp == 's' and you =='w':
        return 0
    elif comp == 'w' and you =='s':
        return 1
    elif comp == 'g' and you == 'w':
        return 1
    elif comp == 'w' and you == 'g':
        return 0
    elif comp =='s' and you == 'g':
        return 1
    elif comp == 'g' and you == 's':
        return 0                   


print("comp turn")
randNo = random.randint(1,3)
print(randNo)

if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'    

you = input("Your Turn: Snake(s) Water(w) or Gun(g)? : ")

print(game(comp,you))