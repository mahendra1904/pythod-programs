#Prime factor
n=int(input('enter the number for factor:   '))
print(n,end=' =')
flag=0
for x in range(2,n):
    if n%x==0:
        flag=1
        while n:
            if n%x==0:
                print(x,end='*')
                n=n//x
            else:
                x=x+1
                break
if flag==0:
    print('This is a prime number')
        



        
