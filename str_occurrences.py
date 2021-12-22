line=input('Enter the String :   ')
str=input('Enter the String to check :   ')


start=count=0
while True:
    pos=line.find(str,start,len(line))
    if pos!=-1:
        count+=1
        start=pos+len(str)
    else:
        break
    if start >=len(line):
        break
print('No of occurances of ',str, ':',count)
            
