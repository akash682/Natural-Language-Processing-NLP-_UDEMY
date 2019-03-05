inp = input("Enter a number: ")
number1 = int(inp)

inp = input("Enter a number: ")
number2 = int(inp)

print(number1+number2)

# File I/O
#Writing to file

inp = input("Enter some text: ")
with open("textFile.txt","w") as f:
    f.write(inp)

inp1 = input("Append text")
with open("textFile.txt","a") as f:
    f.write(inp1)

with open("textFile.txt","r") as f:
    print(f.read())

