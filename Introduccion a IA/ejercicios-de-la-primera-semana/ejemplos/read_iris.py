import csv

with open('Introduccion a IA\ejercicios-de-la-primera-semana\ejemplos\iris_data.txt') as f:
    data = [tuple(line) for line in csv.reader(f)]

print(data)
