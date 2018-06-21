from data import cou,population,population_size
import random
import sys

# population size = 200
# initial population = 1400
# tournment size e= 25% i.e., 350
# at the end new population contains 200 items
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

print(population1)
