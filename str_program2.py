#String program 2:
s=input('Enter any String :   ')
sum=0
w=''
p=''
for i in range(len(s)):
    if s[i].isdigit()==True:
        w=w+s[i]
        sum=sum+int(s[i])
    elif s[i].isalpha==True:
        p=p+s[i]
if s.isalpha()==True:
    print(s,'has no digit : ')
else:
    print(s,'has the digits',w,'which sum to ',sum)





