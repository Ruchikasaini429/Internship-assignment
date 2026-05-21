#dictionary
Dict = {} 
print(Dict) 
Dict[0] = 'Python' 
Dict[2] = 'Java' 
Dict[3] = 1 
print(Dict) 
del(Dict[3])
dict2 = Dict.copy() 
print(dict2) 
Dict.clear() 
print(Dict) 
print(dict2.get(1)) 
print(dict2.items()) 
print(dict2.keys()) 
dict2.pop(2) 
print(dict2) 
dict2.popitem() 
print(dict2) 
dict2.update({3: "Scala"}) 
print(dict2) 
print(dict2.values())

#sets
Set = set()
print(Set)
Set.add(1)
Set.add(2)
Set.add(3)
print(Set)
Set.remove(2)
print(Set)
Set.discard(3)
print(Set)
Set.clear()
print(Set)
a={1,2,3}
b={3,4,5}
print(a|b)
print(a.union(b))
print(a&b)
print(a.intersection(b))
print(a-b)
print(a.difference(b))
print(a^b)
print(a.symmetric_difference(b))

#tuples
Tuple = (1, 2, 3, 4, 5)
print(Tuple)
print(Tuple[0])
print(Tuple[1:4])
print(Tuple + (6, 7, 8))
print(Tuple * 2)

# Concatenation
a = (1, 2)
b = (3, 4)
print(a + b)

# Repetition
print(a * 3)

# Count
x = (1, 2, 2, 3)
print(x.count(2))

# Index
print(x.index(3))

# Nested Tuple
nested = ((1, 2), (3, 4))
print(nested)

# Tuple Packing
person = ("Ruchika", 20, "Python")
print(person)

# Tuple Unpacking
name, age, course = person
print(name)
print(age)
print(course)

# Convert List to Tuple
lst = [1, 2, 3]
tup = tuple(lst)
print(tup)

# Convert Tuple to List
tup2 = (4, 5, 6)
lst2 = list(tup2)
print(lst2)



