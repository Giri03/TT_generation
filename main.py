from data import subjects, days, meettime, rooms, labs, years
from collections import Counter
import random
import sys

population_size_sub = 100
population_size_lab = 50
population = []

def create_population():

    population_sub = []
    population_lab = []
    for j in range(population_size_sub):
        l = -1
        for k in subjects:
            l += 1
            for i in k:
                p = random.choice(i[1])
                if(p[1] == 'AB'):
                    population_sub.append([years[l][0], i[0], p[0], random.choice(['A', 'B']), random.choice(rooms), random.choice(days), random.choice(meettime[0]), -1])
                else:
                    population_sub.append([years[l][0], i[0], p[0], p[1], random.choice(rooms), random.choice(days), random.choice(meettime[0]), -1])
    for j in range(population_size_lab):
        l = -1
        for k in labs:
            l += 1
            for i in k:
                p = random.choice(i[1])
                if(p[1] == 'AB'):
                    population_lab.append([years[l][0], i[0], p[0], random.choice(['A', 'B']), random.choice(days), random.choice(meettime[1]), -1])
                else:
                    population_lab.append([years[l][0], i[0], p[0], p[1], random.choice(days), random.choice(meettime[1]), -1])

    population.append(population_sub)
    population.append(population_lab)
    return population

s = create_population()
