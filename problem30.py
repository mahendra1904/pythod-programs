n=int(input('enter a no :  '))
print('1  = 1')
for x in range(2,n+1):
    for y in range(2,x):
        if x%y==0:
            print(x,'=',end=' ')
            for i in range(2,x):
                while x>0:
                    if x%i==0:
                        print(i,end='*')
                        x=x//i
                    else:
                        break

            
            print()
            break

    else:
        print(x,'= prime()')
