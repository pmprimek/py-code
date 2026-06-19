name = ["apple" ,"orange", 5, 5.32, "prince", " "]
name.append("harry")     # add harry in the end
print(name)

l1 = [1,32,64,7,3]
l1.sort()     # sort() means incresing order
print(l1)

l1 = [1,32,64,7,3]
l1.reverse()      # reverse() the value
print(l1)

l1 = [1,32,64,7,3]
l1.insert(3,8)    # this will add 8 at 3 index
print(l1)

l1 = [1,32,64,7,3]
l1.pop(3)         # will delete element at index 3  and returns its value
print(l1)

l1 = [1,32,64,7,3]
value = l1.pop(3)
print(value)

l1 = [1,32,64,7,3]
l1.remove(64)
print(l1)