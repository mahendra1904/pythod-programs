#Change case of a string 
s=input('Enter the string :   ')
l=len(s)
w=''
for ch in range(0,l):
    if s[ch].islower():
        w=w+s[ch].upper()
    elif s[ch].isupper():
        w=w+s[ch].lower()
    elif s[ch].isalpha==False:
        w=w+s[ch]
    elif s[ch]==' ':
        w=w+s[ch]
    
print(w)
