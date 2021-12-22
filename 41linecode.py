a=int(input("Enter a number A: "))#20
b=int(input("Enter a number B: "))#15
c=int(input("Enter a number C: "))#10
if a>b and a>c:
    print("Highest Number =",a)
    if  b>c:
        print("Next Higher number=",b)
    else:
        print("Next Higher Number =",c)
        if c<b:
            print("Smallest Number=",c)
        else:
            print("Smallest Number",b)

            
elif b>a and b>c:
    print("Highest Number=",b)
    if  c>a:
        print("Next Higher Number=",c)
    else:
        print("Next Higher Number=",a)
        if  a<c:
            print("Smallest Number=",a)
        else:
            print("Smallest number=",c)

            
elif c>a and c>b:
    print("Highest Number =",c)
    if  a>b:
        print("Next Higher Number=",a)
    else:
        print("Next Higher Number=",b)
        if  b<a:
            print("Smallest Number=",b)
        else:
            print("Smallest Number =",a)

            
else :
    print("Enter three different numbers")
