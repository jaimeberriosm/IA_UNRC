import string;
import sys;
import tokenize;

f = open("Introduccion a IA/ejercicios-de-la-cuarta-semana-jaimeberriosm-main/n-grams/don-quijote.txt", 'r')
bigram_freq = {}
word_set_size = 0
line=f.readline() #grabar llinea
while line:
    line = line.rstrip()  #sacar espacios       
    line = line.lower()   #convertir todo a minusculas      
    list = line.split()   # dividir  por caracteres en blanco
    word_set_size += len(list)
    for i in range(len(list) - 1):
        temp = (list[i], list[i+1]) 
        if not temp in bigram_freq.keys():
            bigram_freq[temp] = 1
        else:
            bigram_freq[temp] += 1
    line = f.readline()

sentence = "De lo que contó un cabrero a los que estaban con don"

#TODO Compute the most likely word to continue the sentence, based on bigrams



max1=0
max=0
for word in bigram_freq:
    if bigram_freq[word] > max:
         max=bigram_freq[word]
         max_word=word
print(f'la palabra{max_word} es la mas repetida con {bigram_freq[max_word]} veces')

for pair in bigram_freq:
    if pair[0]=='don':
        print(pair)
        if bigram_freq[pair]>max1:
            max1=bigram_freq[pair]
            max_pair=pair
   
print(f'el par de palabras{max_pair} es el mas probable con {bigram_freq[max_pair]} repeticiones')

