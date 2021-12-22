n=4
print(' '*(n+1)+'*')
for i in range(n):
    print(' '*(n-i)+'*'+' '*(2*i+1)+'*')
for i in range(n):
    print(' '*(i)+'*'+' '*(2*(n-i))+'*')
print(' '*n+'*')
