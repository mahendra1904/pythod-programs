num = eval(input("Enter numerators list :  "))
denum = eval(input("Enter denumerators list :-"))
lst = [ ]
for i in range(len(num)) :
      fraction = num[ i ] / denum[ i ]
      lst.append( fraction )

lst.sort()
print("Smallest fraction = ",lst[ 0 ])
