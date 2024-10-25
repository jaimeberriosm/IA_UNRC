import csv
from statistics import mean,mode,median
with open('Introduccion a IA\ejercicios-de-la-primera-semana\ejemplos\iris_data.txt') as f:
    data = [tuple(line) for line in csv.reader(f)]

data1=[]
data2=[]
data3=[]
data4=[]
data5=[]

l=len(data)

i=0
while i<(l-1):
    data1.insert(i, float(data[i][0]))
    data2.insert(i, float(data[i][1]))
    data3.insert(i, float(data[i][2]))
    data4.insert(i, float(data[i][3]))
    data5.insert(i,data[i][4])
    i=i+1


print('la media es:',mean(data1),mean(data2),mean(data3),mean(data4))
print('la moda es:',mode(data5))
print('la mediana es:',median(data1),median(data2),median(data3),median(data4),)
print(data[1][0])

