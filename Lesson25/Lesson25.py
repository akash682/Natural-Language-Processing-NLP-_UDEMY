# Importing libraries
import re

X =["This is a wolf #scary",
    "Welcome to the jungle #missing",
    "11322 the number to know",
    "Remember the name s - John",
    "I           love          you"]


for i in range(len(X)):
    X[i] = re.sub(r"\W", " ", X[i])
    X[i] = re.sub(r"\d", " ", X[i])
    X[i] = re.sub(r"\s+[a-z]\s+", " ", X[i], flags=re.I)
    X[i] = re.sub(r"\s+", " ",X[i])




print(X)