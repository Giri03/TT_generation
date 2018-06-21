from data import cou, population, population_size, meettime, days
from tournment import population1
import random
import sys
#
# for x in population:
#     print(x)
timetable = []
min = sys.maxsize
for i in days:
    for j in meettime:
        min = sys.maxsize
        for s in range(len(population1)):
            table = population1[s]
            if(j==table[4] and i==table[3] and table[5]<min):
                min = table[5]
                remem = table
        timetable.append(remem)
for x in timetable:
    print(x)
