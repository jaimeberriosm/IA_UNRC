import string;
import sys;
import tokenize;

f = open("Introduccion a IA/ejercicios-de-la-cuarta-semana-jaimeberriosm-main/n-grams/don-quijote.txt", 'r')
freq = {}
line=f.readline()
while line:
    line = line.rstrip()
    line = line.lower()
    list = line.split()
    for word in list:
        if freq.get(word):
            freq[word] += 1
        else:
            freq[word] = 1    
    line = f.readline()

sentence_1 = "De lo que contó un cabrero a los que estaban con don Quijote"
sentence_2 = "Cabrero lo de a los que Quijote estaban don con contó un que"

#TODO Compute probability of sentence_1 and sentence_2
probability={}
#for word in list:
#    probability[word]=freq[word]/range(len(list))

print(probability)
print(range(len(list)))

sentence_1=sentence_1.rstrip()
sentence_1= sentence_1.lower()
sentence_1= sentence_1.split()
prob=1.0
#for word in sentence_1:
#    prob=probability[word]*prob

print(f'La probabilidad de la secuencia uno es {prob}')    

#TODO What is the most likely way of continuing "De lo que contó un"

