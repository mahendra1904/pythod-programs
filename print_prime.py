#x+x^2/2!+x^3/3!+x^4/4!......
x=int(input("Enter a number "))
sum=x
fact=1
for y in range(1,6):
    fact=fact*y
    sum=sum+pow(-x,y)/fact
print(sum)