from data import subjects, days, meettime, rooms, labs, years, divs
from main import create_population
from collections import Counter
import random
import sys

def check(lists):
    for i in lists:
        if i < 5:
            return True
        return False

s = create_population()
population_lab = s[1]
lists = [0,0,0,0,0,0]

for d in days:
    for m in meettime[1]:
        for j in population_lab:
            if(j[4] == d and j[5] == m):
                for y in range(3):
                    print(y)
                    if(years[y][0] == j[0]):
                        break
