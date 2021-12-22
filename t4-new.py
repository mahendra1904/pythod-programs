tup= ()

while True :
      roll = int(input("Enter a roll number :- "))
      name = input("Enter name :-")
      mark = input("Enter marks :-")
      tup += ( (roll,name,mark ),)
      user = input("Do you want to quit enter yes =")
      if user == "yes":
            print(tup)
            break
