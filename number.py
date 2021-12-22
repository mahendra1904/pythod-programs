#1+1/1!+1/2!+1/3!+......+1/n!
n=int(input("Enter the number of terms: "))#3
fact=1
sum=1
for x in range(1,n):#1,2
    fact=fact*x
    sum=sum+1/fact
print(sum)
