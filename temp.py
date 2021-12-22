hour=int(input("Enter hour between 1-12: "))
ahead=int(input("Enter number of hours to be calculated ahead: "))
time=hour+ahead
if time >12:
    print("The time after ",ahead,"hours is",time-12,"pm")
else:
    print("Time after ",ahead,"hours is ",time,"am")
