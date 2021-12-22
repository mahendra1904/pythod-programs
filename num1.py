n=int(input("Enter a number "))
sum=0
for x in range(1,n):
    sum=sum+x
    print(x,end='+')
print(n,"=",sum+n)
