n=int(input("Enter a number "))#n=20
for x in range(2,n):#x=(2,3,4,.....,19)
    for y in range(2,x):#x=7,y=2,3,4,5,6
        if x%y==0:
            break
    else:
        print(x)
        
     
              
