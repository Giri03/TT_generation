from data import subjects, days, meettime, rooms, labs
from collections import Counter
import random
import sys

population_size = 200

def create_population():
    population = []
    population_sub = []
    population_lab = []
    l = 0
    population_size = 200
    for j in range(population_size):
        for i in subjects:
            p = random.choice(i[1])
            if(p[1] == 'AB'):
                population_sub.append([i[0], p[0], random.choice(['A', 'B']), random.choice(rooms), random.choice(days), random.choice(meettime[0])])
            else:
                population_sub.append([i[0], p[0], p[1], random.choice(rooms), random.choice(days), random.choice(meettime[0])])    
        for i in labs:
            population_lab.append([i[0], random.choice(i[1]), random.choice(['A', 'B']), random.choice(days), random.choice(meettime[1])])
    population = population_lab.append(population_sub)
    return population

population = create_population()
for c in population:
    for j in c:
        print(c)

