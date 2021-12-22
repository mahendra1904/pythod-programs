
n=int(input('Enter the no of fibonacci series : '))

l1=[0,1]
a=0
b=1
for x in range(n-1):
    c=a+b
    a=b
    b=c
    
    l1.append(c)
print(l1)
    
