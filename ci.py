#Program to calculate compound interest
principle=int(input("Enter principle "))
rate=int(input("Enter rate "))
time=int(input("Enter time "))
amount=principle*(1+rate/100)**time
ci=amount-principle
print(ci)
