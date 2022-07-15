import random

randno = random.randint(1,100)

userguess = None
guess = 0
while(userguess!=randno):
    userguess = int(input("enter your guess: "))
    guess+=1
    if(userguess==randno):
        print("congrats")
    elif(userguess>randno):
        print("enter a smaller number")
    else:
        print("enter a bigger number")
print(f"You guessed the number in {guess} guesses")                