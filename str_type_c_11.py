#11 type c
str=input('Enter the  String:    ')
l=len(str)
count=0
for x in str:
    if x.isspace()==True:
        count+=1
print('Number of words in string is =: ',l-count)
    
        
    
