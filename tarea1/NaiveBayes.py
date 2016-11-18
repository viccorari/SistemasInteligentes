import numpy as np
import pprint as pp
import copy

data = []
test = []
tables = {}

attributes = [
["vhigh", "high", "med", "low"],
["vhigh", "high", "med", "low"],
["2", "3", "4", "5more"],
["2", "4", "more"],
["small", "med", "big"],
["low", "med", "high"]
]

values = ["unacc", "acc", "good", "vgood"]

indexVal = 6
Pvalues = [0.0]*len(values)

with open("car.data", "r") as filestream:
    for line in filestream:
        line = line.strip('\n')
        currentline = line.split(",")
        data += [currentline]

with open("car-prueba.data", "r") as filestream:
    for line in filestream:
        line = line.strip('\n')
        currentline = line.split(",")
        test += [currentline]

for i in data:
    Pvalues[values.index(i[indexVal])]+=1.0
for v in range(len(values)):
    Pvalues[v] /= len(data)

one = (1.0/len(data))

for v in values:
    t = []
    c = 0
    for i in attributes:
        t += [{}]
        for j in i:
            t[c][j] = 0.0001
        c += 1
    tables[v] = t

for d in data:
    for j in range(len(attributes)):
        tables[d[indexVal]][j][d[j]]+= 1.0

for v in values:
    for i in range(len(attributes)):
        count = 0
        for k in tables[v][i]:
            count += tables[v][i][k]
        for k in tables[v][i]:
            tables[v][i][k]/=count
    
testit = []

for i in range(len(test)):
    testit += [copy.copy(Pvalues)]

i = 0
for t in test:
    j = 0
    for v in values:
        for a in range(len(attributes)):
            testit[i][j] *= tables[v][a][t[a]]
        j += 1
    i += 1

pp.pprint(tables)
print ('\n')
pp.pprint(testit)
print ('\n')

i=0
for t in testit:
    print '\n',"Data de Prueba:"
    print test[i]
    print "Solucion: ",values[t.index(max(t))]
    i+=1
    
print ('\n')
input('Presione cualquier tecla para salir')


#print Pvalues
#print test 
