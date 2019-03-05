# Non homogeneous collection of elements

list1 = [12,12.8 ,8, "This is a string"]

# Printing a list

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

# Inserting elements
list1.append(50)
print(list1)

list1.insert(0, "Sting number 1")
print(list1)

# Updating list
list1[1] = 20
print(list1)

# Deleting list elements
list1.pop()
print(list1)

del list1[2]
print(list1)

#Length of the list
print(len(list1))

# Iterating List
for index in range(0, len(list1)):
    print(list1[index])

for index in range(0, len(list1)):
    list1[index] = 12

for item in list1:
    print(item)

