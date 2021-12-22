#x+x^2/2!+x^3/3!+x^4/4!......
x=int(input("Enter a number "))
n=int(input("Enter number of terms in the series "))
sum=0
fact=1
for y in range(1,n+1):
    fact=fact*y
    sum=sum+pow(x,y)/fact
print(sum)