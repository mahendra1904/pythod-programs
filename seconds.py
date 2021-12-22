#x-x**2/2+x^3/3-x^4/4.........
x=int(input("Enter a base number "))
n=int(input("Enter the number of terms "))
sum=0
for y in range(1,n+1):
    sum=sum+x**y*pow(-1,y+1)
    print(x**y,end=',')
print('=',sum)

