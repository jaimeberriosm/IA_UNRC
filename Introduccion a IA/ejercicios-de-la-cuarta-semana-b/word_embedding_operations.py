import gensim.downloader as api

word_vectors = api.load("glove-wiki-gigaword-100")

# Compute the most similar words to 'argentinian'
result = word_vectors.similar_by_word('argentinian')
print('Most similar words to \'argentinian\', sorted decreasingly by similarity')
print(result)
print(f'Most similar word: {result[0][0]}, with similarity: {result[0][1]}')

# If argentinian is the gentilic of argentina, what would be that of uruguay?
uruguay_gentilic = word_vectors.most_similar(positive=['uruguay', 'argentinian'], negative=['argentina'])[0][0]
print(f'Computed (argentinian - argentina) + uruguay = {uruguay_gentilic}')

print('which word is out of context among {argentinian, uruguayan, peruvian, icecream}?')
print(word_vectors.doesnt_match("argentinian uruguayan peruvian icecream".split()))

# What would be the female (woman) equivalent of 'king'?
#TODO put your code here

# What would be the female (woman) equivalent of 'nba'?
#TODO put your code here

# (nhl - football) + basketball is...
#TODO put your code here




