item=int(input("Enter the no. of items "))
if item<10:
    print("Total cost = ",item*120)
elif item>=10 and item<=99:
    print("Total cost = ",item*100)
else :
    print("Total cost = ",item*70)
