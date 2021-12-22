n=int(input("enter the number to check :  "))#120
var1=[]
var2=[]
for x in range(2,10000):
    for y in range(2,x):
        if x%y==0:
            break
    else: 
        var1.append(x*(x-19))
        var2.append(x*(x+19))
if n in var1 or n in var2:
    print('yes')
else:
    print('no')
