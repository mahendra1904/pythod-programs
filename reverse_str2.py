#main program
#input= i love you
#output= i evol uoy

str=input('enter the string :  ')

l1=str.split()
#print(l1)
str1=''
l2=[]
for x in l1:
        str1=str1+x[::-1] +" "
print(str1)

















