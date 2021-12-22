str=input('Enter the string : ')
#l1=str.split()
length=len(str)
str1=''
for x in range(length-1):
    if str[x].isspace()==False:
        str1=str1+str[x+1]
#print(str1) # string of removed 1st letter
l1=str1.split()
print(l1)
    
