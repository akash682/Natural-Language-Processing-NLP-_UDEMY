import re

sentence = "I love Avengers Avengers"

print(re.sub(r"Avengers","Justice League", sentence))

print(re.sub(r"[a-z]","0",sentence,5,flags=re.I))
