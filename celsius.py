c=eval(input("Enter temperature in celcius: "))
if c<-273.15:
    print("The temperature is invalid because it is below absolute zero")
elif c==-273.15:
    print("The temperature is absolute zero")
elif c>-273.15 and c<0:
    print("The temperature is below freezing")
elif c==0:
    print("The temperature is at freezing point")
elif c>0 and c<100:
    print("The temperature is in the normal range")
elif c==100:
    print("The temperature is at boiling point")
elif c>100:
    print("The temperature is above boiling point")
