#To find largest number of a list
list=eval(input("Enter a list "))
max=0
length=len(list)
for x in list:
    if x>max:
        max=x
print("The maximum value of the list is ",max)
    
