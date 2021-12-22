
def myfun(l):
    return len(l)
str=input('Enter the  string: ')
l1=str.split()

l1.sort(key=myfun)

length=len(l1)
print(l1[length-1])
    
