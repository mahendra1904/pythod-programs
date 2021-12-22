t1=eval(input("enter the nested tupple : "))#t1=((1,2),(1,2,3))
#print(t1)
l1=len(t1)
s1=0
for x in t1:
    for y in range(len(x)):
        s1=s1+y
    print('mean=' ,s1/len(x))
    s1=0
    print(sum(x)/len(x))
        
        
