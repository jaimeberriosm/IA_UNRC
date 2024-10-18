import string;
import sys;
import tokenize;

f = open("Introduccion a IA/ejercicios-de-la-cuarta-semana-jaimeberriosm-main/n-grams/don-quijote.txt", 'r')
#TODO initialize frequency dictionary 
line=f.readline()
while line:
    line = line.rstrip()
    line = line.lower()
    list = line.split()
    for word in list:
        #TODO increment frequency of word
    line = f.readline()
#TODO Compute most frequent word
