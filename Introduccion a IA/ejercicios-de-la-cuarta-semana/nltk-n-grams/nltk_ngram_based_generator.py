from nltk import word_tokenize, sent_tokenize
from nltk.lm import MLE
from nltk.lm.preprocessing import padded_everygram_pipeline
import nltk


text = open('Introduccion a IA/ejercicios-de-la-cuarta-semana/nltk-n-grams/poe.txt', encoding = 'utf8').read()
tokenized_text = [list(map(str.lower, word_tokenize(sent))) 
                  for sent in sent_tokenize(text)]

n = 5
train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
model = MLE(n)
model.fit(train_data, padded_sents)
print(' '.join(model.generate(20)))

