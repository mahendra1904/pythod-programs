n=int(input("Enter a number"))#123
rev=0
temp=n
while n>0:#n=123,12,1
    rem=n%10#3,2,1
    rev=rev*10+rem#3,32,321
    n=n//10#12,1,0
if temp==rev:
    print("The given number is palindrome number")
else:
    print("The number is not palindrome number")
    
