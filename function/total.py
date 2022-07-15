def percent(marks):
    total =0
    for i in range(len(marks)):
        total+=marks[i]
    return (total/len(marks))

marks1 =[32,54,6,13,67]
marks2 = [67,90,93,43,67]

perc = percent(marks1)
print(perc)
perc2 = percent(marks2)
print(perc2)
