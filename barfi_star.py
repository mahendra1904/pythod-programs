#Full Barfi
n=int(input('Enter the number of rows :   '))
for i in range(n):
        print(' '*(n-i)+'* '*(i+1))

for j in range(1,n+1):
    print(' '*(j+1)+'* '*(n-j))
    
