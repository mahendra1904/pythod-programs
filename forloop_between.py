n=int(input("Enter a number "))
m=int(input("Enter a number for divisibility: "))
for x in range(0,n,m):
    if x%2==0:
        print(x,"Divisible by",m,"is even")
    else:
        print(x,"Divisible by ",m,"is odd")
