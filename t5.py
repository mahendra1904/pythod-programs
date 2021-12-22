t=()
for i in range(3):
    mark1=int(input('enter the marks of first subject :'))
    mark2=int(input('enter the marks of 2 subject :'))
    mark3=int(input('enter the marks of 3 subject :'))
    mark=(mark1,mark2,mark3)
    t=t+(mark,)
print(t)
