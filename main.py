from datas import subjects, days, meettime, rooms, labs
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


