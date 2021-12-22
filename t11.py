seq_a=eval(input('enter a tupple : '))#(1,2,3)
seq_b=eval(input('enter a tupple : '))#(1,2,3)
for x in seq_a:
        if x in seq_b:
            print('ture')
        else:
            print('false')
#######################

tup1 = eval(input("enter first tuple = "))

tup2 = eval(input("enter second tuple = "))

count = 0

if len(tup1)==len(tup2):

    for i in range(len(tup1)) :

        if tup1[i] == tup2 [ i ] :

            continue

        else :

            count += 1

    if count == 0  :

        print("True")

    else :

        print("False")

else :
    print("False")
        
