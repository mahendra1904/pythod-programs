#To check the prime number
n=int(input("Enter a number "))
flag=0
for x in range(2,n):
    if n%x==0:
        flag=1
        break
if flag==0:
    print("The entered number",n,"is a prime number")
else:
     print("The entered number",n,"is not a prime number")
    
