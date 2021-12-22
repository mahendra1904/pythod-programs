l1=eval(input('enter the list'))
l=len(l1)
for x in range (l):
    if l1[x]>10:
       l1[x]=10
    
print(l1)
