e = set()   #dont use s = {} as it will creat an empty dictionary

s = {1,2,3,5,5,5,2,}
print(s)
print(s,type(s))

# Set Methods

s.add(556)      # add element
print(s)

s.remove(5)     # update the set s and remove 5 from s
print(s)

s.pop()      # remove element from s random
print(s)

s.clear()     # empties the set s
print(s)

