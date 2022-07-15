sub1 = int(input(" marks: "))
sub2 = int(input(" marks: "))
sub3 = int(input(" marks: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("failed!!")

elif((sub1 + sub2 + sub3)/3 <40):
    print("failed")
else:
    print("pass")