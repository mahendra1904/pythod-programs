import statistics 
t1 = eval(input("Enter a tuple : "))#(1,2,3,4,4,5,6,7,8,7,7,7,6,7,9,7,8,7)
count=0
#sum = sum(tup)
#print("Average =", sum / len( tup ))
for x in t1:
    for y in t1:
        if x==y:
            count+=1
    print(x, '  occur at  ',count, ' times ')
    count=0
    

print("Mode =", statistics.mode( t1 ) )
