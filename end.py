a=eval(input("Enter a positive integer: "))
b=a%10
if b==4:
    print("The number ends with 4")
elif b==8:
    print("The number ends with 8")
else:
    print("Ends with neither 4 nor 8")
