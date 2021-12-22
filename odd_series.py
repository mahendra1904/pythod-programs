#1^2-3^2+5^2-7^2....
n=int(input("Enter number of digits: "))
sum=0
temp=1
for x in range(1,n+1):
    temp=temp*pow(-1,x+1)
    if x%2==1:
        sum=sum+x**2*temp
        print(x**2,end=',')
print('=',sum)
