l=eval(input('Enter the list : '))
l1=[]
len1=len(l)
for x in range(0,len1-1):
    l1.append(l[x])
l1.insert(0,l[len1-1])
print(l1)
    
