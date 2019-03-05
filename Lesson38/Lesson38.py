# Bag of Words Model

# It is going to rain today
# Today I am not going outside
# I am going to watch the season premiere

# Preprocess
# convert into lower case
# Tokenize
# how many times it appears in sentence, build histogram


# it: 1, is: 1, going: 1, to: 1, rain: 1, today:1
# it: 1, am: 1 not: 1, it:,1, is:1, going:2, to:1, rain:1, today:2, outside:1
# ...

# Doesn't count all the numbers
# Reduce non-frequent words.

#       going   to  today   i   am  it  is  rain    not outside
#   1   1       1   1       0   0   1   1   1       0   0
#   2   1       0   1       1   1   0   0   0       1   1
#   3   1       1   0       1   1   0   0   0       0   0