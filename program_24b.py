#Star Pattern
n=int(input('enter the number of rows:    '))
for i in range(n):
    print('*'*(i+1))
for j in range(n):
    print('*'*(n-(j+1)))
