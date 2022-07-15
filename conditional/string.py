text = input("enter text")
spam = False
if("make a lot of money" in text):
    spam = True
elif("buy now " in text):
    spam = True

if(spam):
    print("full scam")
else:
    print("not scam")        
