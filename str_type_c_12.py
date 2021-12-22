#12 type c
str=input('Enter the formula:    ')
count1=count2=0
for x in str:
    if x=='(':
        count1+=1
    elif x==')':
        count2+=1
if count1==count2==1:
    print('Correct formula')
else:
    print('Wrong Formula')
        
    
