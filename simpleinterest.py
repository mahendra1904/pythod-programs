#Mean median Mode
import random
import statistics
a=random.randrange(10,20)
b=random.randrange(20,25)
c=random.randrange(10,20)
d=random.randrange(20,45)
e=random.randrange(10,30)
f=random.randrange(20,25)
t=(a,b,c,d,e,f)
print("The six numbers are ",t)
print("Mean= ",statistics.mean(t))
print("Median= ",statistics.median(t))
print("Mode= ",statistics.mode(t))
