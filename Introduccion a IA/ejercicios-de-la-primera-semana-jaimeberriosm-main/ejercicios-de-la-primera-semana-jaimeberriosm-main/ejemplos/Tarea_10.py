import csv

with open('./iris_data.txt') as f:
    data = [tuple(line) for line in csv.reader(f)]
dict={}
i=0
l=len(data)
while i<l-1:
    u={'clase1':data[i][0],'clase2':data[i][1],'clase3':data[i][2],'clase4':data[i][3],'tipo':data[i][4]}
    dict.update(u)
    i=i+1

for x, obj in dict.items():
    print(x)

    for y in dict.values():
       print(y)