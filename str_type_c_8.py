#8 type c


str=input('Enter the String:    ')
num=int(input('Enter the Number : '))
str1=''
for x in str:
    if x.isdigit()==True:
        str1+=x
    else:
        str1=str1+'0'
num1=int(str1)
print(num, ',' , str,'-->',num,'+',num1,'=',num+num1)        

    
