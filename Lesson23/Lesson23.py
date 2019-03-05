import re

sentence1 = "Welcome to the year 2018"
sentence2 = "Just ~% +++--- arrived at @Jack's place. #fun"
sentence3 = "I                   love                   you"


sentence1_mod = re.sub(r"\d","",sentence1)
print(sentence1_mod)
sentence2_mod = re.sub(r"[@#~%+-\.\']","",sentence2)
print(sentence2_mod)
# WORD Character class
#a-zA-Z0-9
sentence2_mod = re.sub(r"[\W]"," ",sentence2)
print(sentence2_mod)

sentence2_mod = re.sub(r"\s+", " ", sentence2_mod)
print(sentence2_mod)

sentence2_mod = re.sub(r"\s+[a-zA-Z]\s+", " ", sentence2_mod)
print(sentence2_mod)

sentence3_mod = re.sub(r"\s+love\s+", " hate ", sentence3)
print(sentence3_mod)

