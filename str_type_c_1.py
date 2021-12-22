#Number of times  a charater occuers in string :
str=input('Enter the string :   ')
l=len(str)
count=0
for x in range(l):
    for y in range(l):
        if str[x]==str[y]:
            count=count+1
    
    print(str[x], ' occued at ' , count, ' times')
    count=0

##############################2nd method
str1=input('enter the string :  ')
for i in str1:
    print(i,'=',str1.count(i),'times')

        
        
        
        
            
