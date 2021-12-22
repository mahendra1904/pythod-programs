# input the string and give the number of wors
str=input('Enter the string : ')
count=0
for x in str:
    if x.isspace()==True:
        count+=1
        
print('Number of words in the string is : ', count+1)
