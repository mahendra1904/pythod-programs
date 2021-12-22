import statistics
import random
a=random.randrange(100,200,7)
b=random.randrange(100,200,7)
c=random.randrange(100,200,7)
d=random.randrange(100,200,7)
e=random.randrange(100,200,7)
f=random.randrange(100,200,7)
t=a,b,c,d,e,f
print("The numbers are ",t)
print("Mean= ",statistics.mean(t))
print("Median= ",statistics.median(t))
print("Mode= ",statistics.mode(t))
