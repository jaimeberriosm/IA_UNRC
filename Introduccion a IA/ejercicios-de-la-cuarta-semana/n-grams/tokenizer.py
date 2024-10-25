import string;
import sys;
import tokenize;

f = open("Introduccion a IA/ejercicios-de-la-cuarta-semana/n-grams/don-quijote.txt", encoding="utf-8")
#TODO initialize frequency dictionary 
freq={}
line=f.readline()
while line:
    line = line.rstrip()
    line = line.lower()
    list = line.split()
    for word in list:
        #TODO increment frequency of word
        if freq.get(word):
            freq[word]+=1
        else:
            freq[word]=1
    line = f.readline()
#TODO Compute most frequent word
max=0
for word in freq:
    if freq[word] > max:
         max=freq[word]
         max_word=word


print(f' Palabra: "{max_word}" se repite {max} veces')