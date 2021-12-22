#print M in the form of star........
n=10
for x in range(8):
    for y in range(12):
        if (y==0 or y==5) or (x==1 and y==1) or (x==2 and y==2) or (x==1 and y==3):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
        
