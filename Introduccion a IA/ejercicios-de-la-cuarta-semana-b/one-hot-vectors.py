import numpy as np
 
with open('Introduccion a IA/ejercicios-de-la-cuarta-semana-b/rue-morgue.txt', encoding = 'utf8') as text:
    corpus = text.readlines()

# Create a set of unique words in the corpus
unique_words = set()
for sentence in corpus:
    for word in sentence.split():
        unique_words.add(word.lower())
 
# map each unique word to a vector index
word_to_index = {}
for i, word in enumerate(unique_words):
    word_to_index[word] = i

# Print the one-hot encoded vector for the following word:
study = 'study,'
study_vector = np.zeros(len(unique_words))
study_vector[word_to_index[study]] = 1
print(f'The word \'{study}\' is encoded with vector {study_vector}.')

# Print the one-hot encoded vectors for the following sentence:
sentence = 'much invigorated by mathematical study, and especially by that highest branch'
#TODO Put your code here
words = sentence.lower().split()
for word in words:
    word_vector=np.zeros(len(unique_words))
    word_vector[word_to_index[word]] = 1
    print(f'The word \'{word}\' is encoded with vector {word_vector}.')