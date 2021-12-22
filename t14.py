import statistics 
tup = eval(input("Enter a tuple :-"))

sum = sum(tup)
print("Average =", sum / len( tup ))

print("Mean =", statistics.mean( tup ) )
