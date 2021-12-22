#Reverse of three digit number
number=eval(input("Enter the three digit number"))
first=number//100
b=number//10
second=b%10
third=number%10
reverse=third*100+second*10+first
print(reverse)
