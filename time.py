f=eval(input("Enter 1st side of a triangle "))
s=eval(input("Enter 2nd side of a triangle "))
t=eval(input("Enter 3rd side of a triangle "))
if f<=0 or s<=0 or t<=0:
    print("Please enter positive sides of a triangle")
elif f+s>t or s+t>f or t+f>s:
    print("These three sides will form a triangle")
else:
    print("These sides will not form a triangle")

