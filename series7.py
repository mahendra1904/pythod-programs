n=int(input("Enter a number "))
sum=0
for x in range(1,n):
    sum=sum+x**2
    print(x**2,end='+')
print(n**2,"=",sum+n**2)
