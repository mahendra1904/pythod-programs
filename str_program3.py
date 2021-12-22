#Enter the string for all detail
s=input('Enter the string :  ')
l=len(s)
count=0
print(s,'has total number of words : ', l)
for ch in range(l):
    if s[ch].isalpha()==True:
        count+=1
print(s,'has number of charaters = : ', count)
per=count/l*100
print(per,end='%')
