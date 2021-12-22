#String program
s=input('Enter the string:   ')
n=int(input('enter the number :  '))
l=len(s)
w=''
for ch in range(l):
    if s[ch].isdigit()==True:
        w=w+s[ch]
sum=0
sum=sum+n+int(w)
print(sum)
