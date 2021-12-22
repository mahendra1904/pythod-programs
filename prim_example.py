# prime number beween 15 to 25
for x in range(15,25):
    for y in range(2,x):
        if x%y==0:
            
            break
    else:
        print(x,'is a prime number ')
