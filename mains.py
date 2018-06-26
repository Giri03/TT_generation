from data import course, days, meettime
from collections import Counter
import random
import sys

population_size = 200

def create_population():
    population = []
    l = 0
    population_size = 200
    for j in range(population_size):
        for i in course:
            population.append([l , i[0], random.choice(i[2]), random.choice(days), random.choice(meettime), 0])
            l = l + 1
    return population

def fitness(population):
    count = 0
    for i in days:
        for j in meettime:
            cou = Counter(population[s][2] for s in range(len(population)) if population[s][4] == j and population[s][3] == i )

    # extracting from counter dictionary
    for i in population:
        for j,k in cou.items():
            if j == i[2]:
                i[5] = k
    return population

def tournament(population):
    tournment_size = 350
    # some max no.
    cross = []
    # algo
    # iterate 200 time
    # for each iteration choose 350 random elements from overall population
    population1 = []
    for i in range(population_size):
        min = sys.maxsize
        for j in range(tournment_size):
            cross = random.choice(population)
            # print(len(cross))
            if(min > cross[5]):
                min = cross[5]
        population1.append(cross)
    return population1

def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def crossover(population1):
    pc = 0.7
    # here selection is list obtained after tournament selection
    for i in range(0, 200, 2):
        if random.random() > pc:
            if(random.choice([True, False])):
                swap(population1[i][4], population1[i+1][4])
            if(random.choice([True, False])):
                swap(population1[i][5], population1[i+1][5])
    return population1

def mutation(population1):
    pm = 0.2
    for i in range(0, 200, 2):
        if random.random() < pm:
            if(random.choice([True, False])):
                swap(population1[i][4], random.choice(days))
            if(random.choice([True, False])):
                swap(population1[i][5], random.choice(meettime))
    return population1

def new_population(population, population1):
    # create new population .. here range for new population should be 25% of original ..so 200 from crossover and mutation + 150
    for i in range(150):
        population1.append(random.choice(population))
    population = population1
    return population

def timetables(population):
    timetable = []
    for i in days:
        for j in meettime:
            min = sys.maxsize
            for s in range(len(population)):
                table = population[s]
                if(j==table[4] and i==table[3] and table[5]<min):
                    min = table[5]
                    remem = table
            timetable.append(remem)
    return timetable

def change_fitness(population):
    for x in population:
        x[5] = 0
    return population

if __name__ == '__main__':
    population = create_population()
    for i in range(100):
        population = fitness(population)
        population1 = tournament(population)
        population1 = crossover(population1)
        population1 = mutation(population1)
        population1 = change_fitness(population1)
        population1 = fitness(population1)
        population = new_population(population, population1)
        timetable = timetables(population)
        timetable = change_fitness(timetable)
        timetable = fitness(timetable)

    for u in timetable:
        print(u)
