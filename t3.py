t1=()
while True:
    s_roll_number=int(input("Enter the roll no: "))
    s_name=input("enter name of the students : ")
    s_marks=int(input("enter the marks : "))
    t1=t1+(s_roll_number,s_name,s_marks)
    option=input("Do u want to stop :  ::::: press :- :  yes other wise continue : ")
    if option=='yes':
        print(t1)
        break
    else:
        continue
    
