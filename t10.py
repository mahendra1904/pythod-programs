
tup = ((2,5),(4,2),(9,8),(12,8))
count = 0
for  i in range (len(tup)):
    if tup [i][0] % 2 == 0 and tup[i][1] % 2 == 0:
        count += 1
print("the number of pair (a,b) such that a and b are even = ",count)
