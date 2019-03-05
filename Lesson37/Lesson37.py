import nltk

paragraph = "I'm studying at University of Texas at Arlington"

words = nltk.word_tokenize(paragraph)
tagged_words = nltk.pos_tag(words)

namedEnt = nltk.ne_chunk(tagged_words)
namedEnt.draw()

print("Hello")
