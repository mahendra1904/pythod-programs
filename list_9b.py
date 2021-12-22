#enter the list[1,2,3,4444,555,6666]
#output [1, 2, 3, 16, 15, 24]

l1=eval(input('enter the list'))
length=len(l1)
#print(length)
l2=[]
sum=0
for x in l1:
    while x>0:
        rem=x%10
        sum=sum+rem
        x=x//10
    #print(sum)
    l2.append(sum)        
    sum=0
print(l2)
        
    
