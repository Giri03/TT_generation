from data import subjects, days, meettime, rooms, labs, years
from collections import Counter
import random
import sys

population_size = 200

def create_population():
    population = []
    population_sub = []
    population_lab = []
    l = 0
    population_size_sub = 5
    population_size_lab = 2
    for j in range(population_size_sub):
        for y in years:
            no_sub = len(y[1])
            for d in range(no_sub):            
                for i in subjects:
                    p = random.choice(i[1])
                    if(p[1] == 'AB'):
                        population_sub.append([y[0], i[0], p[0], random.choice(['A', 'B']), random.choice(rooms), random.choice(days), random.choice(meettime[0])])
                    else:
                        population_sub.append([i[0], p[0], p[1], random.choice(rooms), random.choice(days), random.choice(meettime[0])])    
    for j in range(population_size_lab): 
        for y in years:
            no_lab = len(y[2])
            for d in range(no_lab):
                for i in labs:
                    population_lab.append([y[0], i[0], random.choice(i[1]), random.choice(['A', 'B']), random.choice(days), random.choice(meettime[1])])

    population = population_lab + population_sub
    return population

population = create_population()
for c in population:
    for j in c:
        print(c)

# create_population()

def fitness(population):
    # finding conflicts in population_sub i.e between the subjects 
    # for a particular day and timeslot, teachers and room shouldn't repeat
    
    count = 0
    for k in days:
        for j in meettime[0]:
            count_sub = dict((i, a.count(i)) for i in population if i[])
            cou = Counter(population[s][2] for s in range(len(population)) if population[s][4] == j and population[s][3] == i )

    # extracting from counter dictionary                  
    for i in population:
        for j,k in cou.items():
            if j == i[2]:
                i[5] = k 
    return population