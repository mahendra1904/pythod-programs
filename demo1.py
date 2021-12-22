#9 type c
str1=input('Enter the 1st  String:    ')
str2=input('Enter the 2st  String:    ')
if str1<str2:
    print(str2)
else:
    l=len(str1)
    for x in range(l//2):
        print(' '*x+str1[x]+' '*(l-(2*(x+1)))+str1[-(x+1)])
        
        
    
