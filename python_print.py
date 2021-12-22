#Print python
s='python'
l=len(s)
for i in range(l+1):
    for j in range(i):
        print(s[j],end='')
    print()
