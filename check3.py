#Print the Star in some specific pattern
l1=10
for i in range(0,l1//2):
    print(' '*i+'*'+  ' '*pow(2,(l1//2-(i+1)))+'*'*(-(i+1)))
