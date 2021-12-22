#7type c



while True:
    str=input('Enter the String:    ')
    if str=='q' or str=='Q':
        break
    l=len(str)
    str1=''
    for x in str:
        if x.islower()==True:
            str1=str1+x.upper()
        elif x.isupper()==True:
            str1=str1+x.lower()
        else:
            str1=str1+x
    print(str1)
        
    
