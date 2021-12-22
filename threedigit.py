f=eval(input("Enter the length of 1st side of a triangle "))
s=eval(input("Enter the length of 2nd side of a triangle "))
t=eval(input("Enter the length of 3rd side of a triangle "))
if f==s==t:
    print("The triangle is equilateral")
elif f!=s and t!=f and s!=t:
    print("The triangle is scalene")
else :
    print("The triangle is isoceles")
