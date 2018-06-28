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

def labs_labs(population_lab):
    for d in days:
        for m in meettime[1]:
            for j in population_lab:
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
                for k in population_lab:
                    if(k[4] == d and k[5] == m):
                        k[-1] = k[-1] + sum(lists) - 2
    return population_lab
s = labs_labs(population_lab)
print(s)

# cross over for actual tt

population_lab_size = 100
population_sub_size = 100
# for lectures
for i in range(0, population_sub_size , 2):
    if random.random() > pc:
        if(random.choice([True, False])):
            swap(selection[i][4], selection[i+1][4])# rooms
        if(random.choice([True, False])):
            swap(selection[i][6], selection[i+1][6])# slot
        if(random.choice([True, False])):
            swap(selection[i][5], selection[i+1][5])# days

# for labs
for i in range(0, population_lab_size , 2):
    if random.random() > pc:
        if(random.choice([True, False])):
            swap(selection[i][6], selection[i+1][6])# slot
        if(random.choice([True, False])):
            swap(selection[i][5], selection[i+1][5])# days

# mutation

def mutation(population1):
    pm = 0.2

    for i in range(0, population_sub_size, 2):
        if random.random() < pm:
            if(random.choice([True, False])):
                swap(population1[0][i][4], random.choice(rooms))# rooms
            if(random.choice([True, False])):
                swap(population1[0][i][6], random.choice(meettime[0]))# slots
            if(random.choice([True, False])):
                swap(population1[0][i][5], random.choice(days))# days

    pm = 0.2
    for i in range(0, population_lab_size, 2):
        if random.random() < pm:
            if(random.choice([True, False])):
                swap(population1[1][i][5], random.choice(days))# days
            if(random.choice([True, False])):
                swap(population1[1][i][6], random.choice(meettime[1]))# slots

    return population1

# timetable generation
# sort population according to no. of conflicts
# make a list of and add that particulat labs
    # call function to find all such labs at day and time
    # add in tt matrix for that position

sort(population_lab)
for y in years:
    for div in divs:
        for i in range(4):
            # make a list of days in which lab should be uphold
        # call function to find all such labs at day and time
