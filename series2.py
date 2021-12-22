#1^2-3^2+5^2-7^2....
n=int(input("Enter number of digits: "))
sum=0
for x in range(1,n+1,2):
    sum=sum+x**2
    print(x**2,end=',')
print('=',sum)


