# TUPLE
# Same as lists but immutable

tuple1 = (12, "This is a string", 15.9, "Another string")
tuple2 = (50,90.2)


print(tuple1)
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

tuple3 = tuple1 + tuple2
print(tuple3)

print(len(tuple3))

for i in tuple1:
    print(i)

