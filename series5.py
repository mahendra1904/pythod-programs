#Program for simple Interest
p=eval(input("Enter the principle "))
r=eval(input("Enter the rate of interest "))
t=eval(input("Enter the time period of the loan "))
si=(p*r*t)/100
amount=p+si
print("The amount to be paid after the time period of ",t,"years at ",r,"%interest is ",amount)
