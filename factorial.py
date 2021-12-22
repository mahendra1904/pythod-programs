#Factorial of any number
n=int(input("Enter any number: "))
sum=1
for x in range(1,n+1):
    sum=sum*x
print("Factorial of given number",n,"is",sum)
