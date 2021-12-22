# Lowest Number and the second lowest number
sum=small=smaller=0
for x in range(1,11):
    n=int(input("enter the number :  "))
    if x==0:
        small=n
    elif x==1:
        if n<=small:
            smaller=n
        else:
            smaller=small
            small=n
    else:
        if n<smaller:
            small=smaller
            smaller=n
        elif n<small:
            small=n
print('the lowest number is ', small)
print('the 2nd lowest number is : ', smaller)
        
        
    
