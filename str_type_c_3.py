#WAP to reversed the string and store the reverse string in new string
str=input('enter the string :  ')
l=len(str)
str1=''
for x in range(-1,-(l+1),-1):
    str1=str1+str[x]
print(str1)
