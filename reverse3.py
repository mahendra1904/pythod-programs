#1,5,10,17,26...........
n=int(input("Enter a number "))
sum=0
for x in range(0,n):
    sum=sum+x**2+1
    print(x**2+1,end="+")
print("=",sum)
