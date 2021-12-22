# Only Border of the Barfi 
n=int(input('Enter the number of rows :   '))
print(' '*n+'*')
for i in range(1,n):
    print(' '*(n-i)+'*'+' '*(2*i-1)+'*')

for i in range(1,n):
    print(' '*(i)+'*'+' '*(2*(n-i))+'*')
print(' '*(n)+'*')













