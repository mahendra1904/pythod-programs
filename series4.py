#1^3+3^3+5^3....
n=int(input("Enter number of digits: "))
sum=0
for x in range(1,n+1):
    sum=sum+x*x*x*pow(-1,x+1)
    print(x*x*x,end='+')
print('=',sum)


