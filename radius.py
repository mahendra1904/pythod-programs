#Program to find the reversed number
number=int(input("Enter the two digit number "))
q=number//10
rem=number%10
rev=rem*10+q
print("The reverse of the given number",number,"is ",rev)

