n=int(input("Enter a number "))
cube=0
for x in range(1,n):
    cube=cube+x*x*x
    print(x*x*x,end="+")
print(n*n*n,"=",cube+n*n*n)
    
