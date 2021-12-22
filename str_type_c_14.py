#14 type c ##### Biggest word length wise
str=input('Enter the String:   ')
#st= list of words
st=str.split() #list of all words
for x in range(len(st)):
    for j in range(len(st)-1):
        if len(st[j])>len(st[j+1]):
            st[j+1],st[j]=st[j],st[j+1]
print("Longest word in the string =: " ,st[-1])

###########
