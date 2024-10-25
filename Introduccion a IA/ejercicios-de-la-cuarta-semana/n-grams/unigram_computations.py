import string;
import sys;
import tokenize;

f = open("Introduccion a IA/ejercicios-de-la-cuarta-semana/n-grams/don-quijote.txt", encoding="utf-8")
freq = {}
l=0
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
l=len(freq)

for word in freq:
    probability[word]=freq[word]/l


sentence_1=sentence_1.rstrip()
sentence_1= sentence_1.lower()
sentence_1= sentence_1.split()
prob1=1.0
for word in sentence_1:
    prob1=probability[word]*prob1
    print(f'la probabilidad de {word} es {probability[word]}')
print(sentence_1)
print(f'La probabilidad de la secuencia uno es {prob1}')    


entence_2=sentence_2.rstrip()
sentence_2= sentence_2.lower()
sentence_2= sentence_2.split()
prob2=1.0
for word in sentence_2:
    prob2=probability[word]*prob2
    print(f'la probabilidad de {word} es {probability[word]}')
print(sentence_2)
print(f'La probabilidad de la secuencia dos es {prob2}')    

if prob1>prob2:
    print('La primera secuencia es mas probable')
else:
    print('La segunda secuencia es mas probable')

#TODO What is the most likely way of continuing "De lo que contó un"

max=0
for word in freq:
    if freq[word] > max:
         max=freq[word]
         max_word=word


print(f' La palabra "{max_word}" tiene mayor probabilidad de completar la oracion')

