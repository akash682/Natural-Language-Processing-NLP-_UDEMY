import re

sentence = "1996 was the year I was born."

print(re.match(r"[a-zA-Z]+", sentence))
print(re.search(r"[a-zA-Z]+", sentence))

# Starts with
if re.match(r"^1996", sentence):
    print("match")
else:
    print("nomatch")

#Ends with
if re.search(r"born.$", sentence):
    print("match")
else:
    print("nomatch")