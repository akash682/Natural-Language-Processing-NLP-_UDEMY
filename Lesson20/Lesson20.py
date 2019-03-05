import re

sentence = "I was born in the year 1996."
sentence = "abb"

print(re.match(r".*",sentence))
print(re.match(r".+",sentence))

print(re.match(r"[a-zA-Z]+",sentence))
print(re.match(r"ab?",sentence))