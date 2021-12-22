n=int(input('Enter the number of rows :   '))
for i in range(n):
        print(' '*(n-i)+'* '*(i+1))

###########################################
        
#Full Barfi
n=int(input('Enter the number of rows :   '))
for i in range(n):
        print(' '*(n-i)+'* '*(i+1))

for j in range(1,n+1):
    print(' '*(j+1)+'* '*(n-j))
    
########################################
    
#Star Pattern
n=int(input('enter the number of rows:    '))
for i in range(n):
    print('*'*(i+1)+' '*(n-((i+1))))
############################

#Star Pattern
n=int(input('enter the number of rows:    '))
for i in range(n):
    print('*'*(i+1)+' '*(n-((i+1))))
for j in range(n):
    print('*'*(n-(j+1)))

####################################
sum=0
for i in range(1,10):
    for j in range(i):
        sum=sum+pow(10,j)
    print(sum)

############################
