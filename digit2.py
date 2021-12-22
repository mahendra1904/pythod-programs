#Program to find number of digits
x=int(input("Enter an integer "))
count=0
temp=x
while temp>0:
    rem=temp%10
    count=count+1
    temp=temp//10
print("Number of digits=",count)
rem1=x%10
msd=x//10**(count-1)
y=rem1*10+msd
print("Required output=",y)
