import nltk
from nltk import word_tokenize, sent_tokenize

text = open('./poe.txt', encoding = 'utf8').read()
tokenized_text = word_tokenize(text)

# Generate trigrams (n=3)
n = 3
trigrams = list(nltk.ngrams(tokenized_text, n))

# Print the generated trigrams
for trigram in trigrams:
   print(trigram)


