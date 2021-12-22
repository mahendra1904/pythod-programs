l=eval(input('Enter the list : '))
m=eval(input('Enter the list with same size of previous : '))
l1=len(l)
l2=len(m)
n=[]
if l1==l2:
    for i in range(l1):
        for j in range(l2):
            if i==j:
                n.append(l[i]+m[j])
    print(n)
                

    
else:
    print('Give the proper input.....')
