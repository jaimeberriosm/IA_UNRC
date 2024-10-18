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


