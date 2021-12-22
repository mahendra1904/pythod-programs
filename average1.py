list=eval(input("Enter only 5 numbers "))
if len(list)==5:
    average=(list[0]+list[1]+list[2]+list[3]+list[4])/len(list)
    print("The average of the numbers ",list,"is ",average)
elif len(list)>5:
    print("Please Enter only 5 numbers")
elif len(list)<5:
    print("Enter 5 numbers")
