# List Comprehension in Python

numbers = [1,2,3,4,5,6,7,8,9,10]

newNumbers = []
for number in numbers:
    newNumbers.append(number)

newNumbers = [number for number in numbers]

newNumbers = [number for number in numbers if number <=5]

numbers2 = [1,3,5,7,9]

newNumbers = [number for number in numbers if number not in numbers2]

newNumbers = [number*2 for number in numbers]
newNumbers = [number for number in numbers if number%2 == 1]

# Generator Comprehension
squareGen = (number**2 for number in numbers)
list(squareGen)

myDict = {"apple":1, "orange":4, "banana":10}
newDict = {key:myDict[key] for key in myDict.keys()}

newDict ={key:myDict[key] for key in myDict.keys() if myDict[key]>5}

words = {"I", "love", "Avengers"}
sentence = ' '.join(words)
print(sentence)