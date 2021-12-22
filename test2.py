#"ereht era ynam ysad"
x = "there are many days"
length=len(x)
l1=x.split()
str=''
for x in l1:
    str=str+x[::-1]+ ' ' 
print(str)
    
