from data import subjects, days, meettime, rooms, labs, years
from collections import Counter
import random
import sys


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
                        population_sub.append([y[0], i[0], p[0], random.choice(['A', 'B']), random.choice(rooms), random.choice(days), random.choice(meettime[0]), 0])
                    else:
                        population_sub.append([i[0], p[0], p[1], random.choice(rooms), random.choice(days), random.choice(meettime[0]), 0])
    for j in range(population_size_lab):
        for y in years:
            no_lab = len(y[2])
            for d in range(no_lab):
                for i in labs:
                    population_lab.append([y[0], i[0], random.choice(i[1]), random.choice(['A', 'B']), random.choice(days), random.choice(meettime[1]), 0])

    print(population_lab)
    print(population_sub)
    # population = population_lab + population_sub
    # return population

# population = create_population()
# for c in population:
#     for j in c:
#         print(c)

create_population()

def fitness(population):
    # finding conflicts in population_sub ... between the subjects
    # increment conflict count if: for a particular day and timeslot, teacher or room repeats
    count = 0
    for k in days:
        for j in meettime[0]:
            count_tea_conflict = Counter(i[2] for i in population[0] if i[5] == k and i[6] == j)
            count_room_conflict = Counter(i[4] for i in population[0] if i[5] == k and i[6] == j)
            # cou = Counter(population[s][2] for s in range(len(population)) if population[s][4] == j and population[s][3] == i )

    # extracting from counter dictionary
    for i in population[0]:
        for j, k in count_tea_conflict.items():
            if j == i[2]:
                i[5] += k
        for j, k in count_room_conflict.items():
            if j == i[2]:
                i[5] += k
    # Between labs.. increment the conflict count for a particular day and timeslot if more than 2 labs for different years is going on
    for k in days:
        for j in meettime[1]:
            for y in range(len(years)):
                for k in ['A', 'B']:
                    for a in range(y + 1, len(years)):
                        for u in['A', 'B']:
                            x = list(i for i in population[1] if i[5] == k and i[6] == j and (i[0] == years[y] and i[3] == k or i[0] == years[a] and i[3] == u))



    return population
