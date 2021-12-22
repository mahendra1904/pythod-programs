#2/9-5/13+/8/17........
n=2
d=9
sum=2/9
t=int(input("Enter number of terms: "))
for x in range(1,t):
    n=n+3
    d=d+4
    sum=sum+n/d*pow(-1,x)
print(sum)