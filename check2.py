#1^3-3^3-5^3....
n=int(input("Enter number of digits: "))
sum=0
temp=1
for x in range(1,n+1):
    temp=temp*pow(-1,x+1)
    if x%2==1:
        sum=sum+x*x*x*temp
        print(x*x*x,end='-')
print('=',sum)
