# Write a program which replaces all vowels in the string with '*'
str=input('enter the string :  ')
str2='aeiou'
str3='AEIOU'
l=len(str)
str4=''
for x in str:
    if x in str2 or x in str3:
        str4=str4+'*'
    else:
        str4=str4+x
print(str4)
        
