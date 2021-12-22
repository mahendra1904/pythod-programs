low=sec_low=9999999999999999999
#num=[1,2,3,33,4,5,6,77,8,999,8888,44,-9,0,66,99]
for x in range(1,11):
    n=int(input('enter the number :  '))
    if  n<=low:
        low,sec_low=n,low
        
    elif n < sec_low:
        sec_low=n
        

print('lowest :  ', low,  ' 2nd lowest  ',sec_low)
            
