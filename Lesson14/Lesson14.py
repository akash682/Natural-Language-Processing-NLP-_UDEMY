# Key - Value Pairs

dict1 ={}

# Adding elements to the dictionary
dict1['apple'] = "Apple is a fruit"
dict1['orange'] = "Orange is a fruit"
dict1['python'] = "Programming language"
dict1['car'] = "car is a fast moving object"

print(dict1)
print(dict1['apple'])
print(dict1['orange'])
print(dict1['car'])

print(dict1.get("jython", "Key doesn't exist"))

del dict1['apple']
print(dict1)

print(len(dict1))

listOfKeys = list(dict1.keys())
print(listOfKeys)
listOfValues = list(dict1.values())
print(listOfValues)

for key in dict1.keys():
    print(dict1[key])

for value in dict1.values():
    print(dict1.values())
