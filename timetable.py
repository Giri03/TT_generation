from data import meettime, days, course
from new_population import population
# from tournment import population1
import random
import sys
#
# for x in population:
#     print(x)
timetable = []
min = sys.maxsize

tt = []
for j in course:
    min = sys.maxsize
    for s in range(len(population)):
        if(population[s][1] == j[0]):
            table = population[s]
            if(table[5] < min):
                min = table[5]
                remem = table
    tt.append(remem)
            
# print(tt)            

for i in days:
    for j in meettime:
        min = sys.maxsize
        for s in range(len(population)):
            table = population[s]
            if(j==table[4] and i==table[3] and table[5]<min):
                min = table[5]
                remem = table
        timetable.append(remem)
count = 0
for i in range(len(tt)):
    for s in range(len(timetable)):
        if(tt[i][3] == timetable[s][3] and tt[i][4] == timetable[s][4]):
            count += 1
            timetable[s] = tt[i]
            print(s)

print(tt)
for d in timetable:
    print(d)
