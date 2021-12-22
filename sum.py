#sum any number of inputs

count=sum=0
ans='y' or 'Y'
while ans=='y' or ans=='Y':
    n=int(input("enter the number for addition :  "))
    sum=sum+n
    count+=1
    ans=input('want to  enter more values (y/n ) :  ')
  
print(sum)
