#String first program
s=input('Enter a 12 digit contact number in this format xxx-xxx-xxxx :  ')
if len(s)==12:
    if s[3]=='-' and s[7]=='-':
        if s[:2].isdigit() and s[4:7].isdigit() and s[9:].isdigit() ==True:
            print('Number enter is in correct format ')
else:
    print('wrong input, try again.....')
