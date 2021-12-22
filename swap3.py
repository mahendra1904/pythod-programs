a=eval(input("Enter temperature "))
b=eval(input("Enter unit(C or F): "))
if b=="F":
    print(a,"F is ",(a-32)*5/9,"C")
elif b=="C":
    print(a,"C is ",(a*9/5)+32,"F")
