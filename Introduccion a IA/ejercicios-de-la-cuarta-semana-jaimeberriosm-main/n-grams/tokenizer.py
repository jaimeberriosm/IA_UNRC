import string;
import sys;
import tokenize;

f = open("./don-quijote.txt", 'r')
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
