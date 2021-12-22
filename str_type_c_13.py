#13 type c ##### count the number of vowels
str=input('Enter the String    ')
v1='aeiou'
v2='AEIOU'
count=0
for x in str:
    if x in v1 or x in v2:
        count+=1
print('The Number of vowels in the string are:  ', count)
    
