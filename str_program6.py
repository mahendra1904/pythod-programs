#Print the larger string in some specific pattern
s1=input('enter the first string:  ')
s2=input('enter the second string :  ')
l1=len(s1)
l2=len(s2)
if s1>s2:
    for i in range(0,l1//2):
        print(' '*i+s1[i]+  ' '*pow(2,(l1//2-(i+1)))+s1[-(i+1)])
