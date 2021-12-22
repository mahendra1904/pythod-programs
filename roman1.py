num=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
rom=['M','MC','D','CD','C','XC','L','XL','X','IX','V','IV','I']
n=int(input('Enter the number :  '))
roman=''
for x in range(len(num)):
    m=n//num[x]
    for j in range(m):
        roman=roman+rom[x]
    n=n%num[x]
print(roman)
