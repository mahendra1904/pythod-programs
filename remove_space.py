#Remove the white space between the string :
s=input('Enter the string :   ')
l=len(s)
w=''
for ch in range(0,l):
    if s[ch].isalpha()==True:
        w=w+s[ch]
    elif s[ch].isdigit()==True:
        w=w+s[ch]
print(w)
