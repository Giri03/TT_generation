from data import subjects, days, meettime, rooms, labs, years, teachers
from collections import Counter
import random
import sys

population_size_sub = 100
population_size_lab = 50

def create_population():
    population = []
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

def fitness(population):
    # -----------Conflicts for same teachers in different labs at same day and time
    for k in days:
        for j in meettime[1]:
            # print (k + j)
            count_tea_conflict = Counter(i[2] for i in population[1] if i[4] == k and i[5] == j)
            # extracting from counter dictionary                  
            for i in population[1]:
                for key, value in count_tea_conflict.items():
                    if (key == i[2] and i[4] == k and i[5] == j):
                        i[-1] += value
    
    # -----------Conflicts for same teachers in different labs and occupying same room at same day and time 
    for k in days:
        for j in meettime[0]:
            count_tea_conflict = Counter(i[2] for i in population[0] if i[5] == k and i[6] == j)
            count_room_conflict = Counter(i[4] for i in population[0] if i[5] == k and i[6] == j)
            # extracting from counter dictionary                  
            for i in population[0]:
                for key, value in count_tea_conflict.items():
                    if key == i[2] and i[5] == k and i[6] == j:
                        i[-1] += value
                for key, value in count_room_conflict.items():
                    if key == i[4] and i[5] == k and i[6] == j:
                        i[-1] += value

    # ----------- Conflicts btwn lab and theory sub at same time 
    for d in days:
        for i in meettime[1]:
            count_sub = 0
            count_lab = 0    
            for s in population[1]: 
                if s[5] == i and s[4] == d:
                    count_lab += 1 
                    if(count_sub > 0):
                        s[-1] += 1
            for s in population[0]:
                # print(i[6] +i[7])
                if (s[5] == d and int(i[0]+i[1]) <= int(s[6][0]+s[6][1]) < int(i[5]+i[6])) :
                    count_sub += 1
                    if(count_lab > 0):
                        s[-1] += 1
            for s in population[1]:
                if s[4] == d and s[5] == i:
                    s[-1] += 1
    return population
    
def check(lists):
    for i in lists:
        if i < 5:
            return True
        return False

def labs_labs(population):
    lists = [0, 0, 0, 0, 0, 0]
    for d in days:
        for m in meettime[1]:
            for j in population[1]:
                if(j[4] == d and j[5] == m):
                    for y in range(len(years)):
                        if(years[y][0] == j[0]):
                            break
                        if(j[3] == 'A'):
                            lists[y*2]+=1
                        else:
                            lists[y*2+1]+=1
            flag = check(lists)
            sums = 0
            if(flag == True):
                sums = sum(lists) - 2
                if(sums<3):
                    no = "no problem"
            else:
                for k in population[1]:
                    if(k[4] == d and k[5] == m):
                        k[-1] = k[-1] + sum(lists) - 2
    return population  

def tournament(population):
    tournment_size_sub = len(population[0]) / 10
    tournment_size_lab = len(population[1]) / 10
    newpop_sub_size = len(population[0]) / 4
    newpop_lab_size = len(population[1]) / 4
    # some max no.
    cross = []
    # algo
    # iterate 200 time
    # for each iteration choose 350 random elements from overall population
    population1 = []
    population1_sub = []
    population1_lab = []
    for i in range(newpop_sub_size):
        min = sys.maxsize
        for j in range(tournment_size_sub):
            cross = random.choice(population[0])
            # print(len(cross))
            if(min > cross[-1]):
                min = cross[-1]
        population1_sub.append(cross)
    for i in range(newpop_lab_size):
        min = sys.maxsize
        for j in range(tournment_size_lab):
            cross = random.choice(population[1])
            # print(len(cross))
            if(min > cross[-1]):
                min = cross[-1]
        population1_lab.append(cross)
    population1.append(population1_sub)
    population1.append(population1_lab)

    return population1

def swap(a, b):
    a, b = b, a

def crossover(selection):
    pc = 0.57
    population_lab_size = len(selection[1])
    population_sub_size = len(selection[0])
    print(population_lab_size )
    print(population_sub_size)
    print(selection[0][337][4])
    print('#########')
    # for lectures
    for i in range(0, population_sub_size - 1 , 2):
        if random.random() > pc:
            if(random.choice([True, False])):
                print(i)
                swap(selection[0][i][4], selection[0][i+1][4])# rooms
            if(random.choice([True, False])):
                swap(selection[0][i][6], selection[0][i+1][6])# slot
            if(random.choice([True, False])):
                swap(selection[0][i][5], selection[0][i+1][5])# days

    # for labs
    for i in range(0, population_lab_size -1, 2):
        if random.random() > pc:
            if(random.choice([True, False])):
                swap(selection[1][i][6], selection[1][i+1][6])# slot
            if(random.choice([True, False])):
                swap(selection[1][i][5], selection[1][i+1][5])# days
    return selection

def mutation(population1):
    pm = 0.2
    population_lab_size = len(population1[1])
    population_sub_size = len(population1[0])
    for i in range(0, population_sub_size, 2):
        if random.random() < pm:
            if(random.choice([True, False])):
                swap(population1[0][i][4], random.choice(rooms))# rooms
            if(random.choice([True, False])):
                swap(population1[0][i][6], random.choice(meettime[0]))# slots
            if(random.choice([True, False])):
                swap(population1[0][i][5], random.choice(days))# days

    pm = 0.2
    for i in range(0, population_lab_size - 1, 2):
        if random.random() < pm:
            if(random.choice([True, False])):
                swap(population1[1][i][5], random.choice(days))# days
            if(random.choice([True, False])):
                swap(population1[1][i][6], random.choice(meettime[1]))# slots
                
    return population1

def new_population(population, population1):
    # new pop will be 30% of original => 25% from tournament selection + 5% random choice
    per_sub = len(population[0]) / 20
    per_lab = len(population[1]) / 20 
    for i in range(per_sub):
        population1[0].append(random.choice(population[0]))
    for i in range(per_lab):
        population1[1].append(random.choice(population[0]))

    population = population1
    return population

def change_fitness(population):
    for x in population:
        for j in x:
            j[5] = 0
    return population

if __name__ == '__main__':
    population = create_population()
    # print(population)
    population = fitness(population)
    population = labs_labs(population)
    population1 = tournament(population)
    population1 = crossover(population1)
    population1 = mutation(population1)
    print(population1)
    population1 = change_fitness(population1)
    population1 = fitness(population1)
    population = new_population(population, population1)

# pop = create_population()
# pop = fitness(pop)
# pop = labs_labs(pop[1])
# pop1 = tournament(pop)

# print(len(pop1[0]))
# print(pop[0])
