#Program to convert cm in inches
number=eval(input("Enter length in centimetre "))
inch= number/2.54
if number<0:
    print("The entry is invalid, please enter another number")
else:
    print("On converting ",number,"cm into inches we get ",inch)
