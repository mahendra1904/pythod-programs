


lst = eval(input("Enter a list :-"))
dup = [ ]
n = 1
while n < len(lst):
      for i in lst :
            if lst.count( i ) != 1 :
                  lst.remove( i )
                  dup.append(i)
      n += 1

lst.sort()
print("New list :- ",lst + dup)
