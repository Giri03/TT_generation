from data import days, meettime, years, divs, zerohours, free_lec, tp_lecture
from app import *
from collections import Counter
import random
import sys

population_size_sub = 150
population_size_lab = 200
timetable = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
all_time = []

def sortIt(population):
    population[0].sort(key = lambda x:x[-1])
    population[1].sort(key = lambda x:x[-1])
    # print(population)
    return population

def fitness(population):
    # -----------Conflicts for same teachers in different labs at same day and time
    for k in days:
        for j in meettime[1]:
            # print (k + j)
            # print(population)
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
    tournment_size_sub = len(population[0]) // 20
    tournment_size_lab = len(population[1]) // 15
    newpop_sub_size = len(population[0]) // 3
    newpop_lab_size = len(population[1]) // 2
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
    pc = 0.65
    population_lab_size = len(selection[1])
    population_sub_size = len(selection[0])

    # for lectures
    for i in range(0, population_sub_size - 1 , 2):
        if random.random() > pc:
            if(random.choice([True, False])):
                swap(selection[0][i][4], selection[0][i+1][4])# rooms
            if(random.choice([True, False])):
                swap(selection[0][i][6], selection[0][i+1][6])# slot
            if(random.choice([True, False])):
                # print(selection[0][i][5])
                # print(selection[0][i+1][5])
                swap(selection[0][i][5], selection[0][i+1][5])# days

    # for labs
    for i in range(0, population_lab_size -1, 2):
        if random.random() > pc:
            if(random.choice([True, False])):
                swap(selection[1][i][6], selection[1][i+1][6])# slot
            if(random.choice([True, False])):
                swap(selection[1][i][5], selection[1][i+1][5])# days
    return selection


def mutation(population1, rooms_tp):
    pm = 0.45
    population_lab_size = len(population1[1])
    population_sub_size = len(population1[0])
    for i in range(0, population_sub_size, 2):
        if random.random() < pm:
            if(random.choice([True, False])):
                swap(population1[0][i][4], random.choice(rooms_tp))# rooms
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
    per_sub = len(population[0]) // 7
    per_lab = len(population[1]) // 5
    for i in range(per_sub):
        population1[0].append(random.choice(population[0]))
    for i in range(per_lab):
        population1[1].append(random.choice(population[1]))

    population = population1
    return population

def change_fitness(population):
    for x in population:
        for j in x:
            j[-1] = 0
    return population

def getList(pop_id, choice): #
    if(choice == 0):
        for i in population[0]:
            if i[-2]  == pop_id:
                return i
    else:
        for i in population[1]:
            if i[-2] == pop_id:
                return i

def getTime(meet):
    ind = meettime[1].index(meet)
    if meettime[1][-1] == meet:
        meet = meettime[0][ind*2]
        meet += meettime[0][-2]
    else:
        meet = meettime[0][ind*2]
        meet += meettime[0][ind*2+1]
    return meet

def timetables(population, whichsem, room_tp):
    global all_time
    all_time = []
    timetable = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
    lab_matrix = [[2,2,1,1],[2,2,1,1],[2,2,1,1] ,[2,2,1,1],[2,2,1,1]]
    tea_matrix = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
    room_matrix = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
    # sort for minimum conflicts
    population[0].sort(key = lambda x:x[-1])
    population[1].sort(key = lambda x:x[-1])
    # for tplectures
    count_tp = -1
    # frozen constraint
    zero_days = random.sample(days, 2)
    for y in years:
        # set T&P day for year randomly
        zero_time = "03:40-04:40"

        if(y[0] == 'se'):
            zero_day = zero_days[0]
        else:
            zero_day = zero_days[1]
        exclude_zero_day = list(x for x in days if x != zero_day)
        tp_day = random.choice(exclude_zero_day)
        tp_time = random.choice(meettime[0])
        p2_days1 = list(x for x in exclude_zero_day if x != tp_day)
        p2_days = random.sample(p2_days1, 2)
        for div in divs:
            count_free = -1
            count_tp += 1
            timetable = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
            # set p2 for even and Odd
            if(y[0] == 'be' and div == 'A' and whichsem == 'Even'):
                for tmng in range(7):
                    timetable[days.index(p2_days[0])][tmng].append(['', 'P2', '', '', '', '', '', 'S-', ''])

            elif (y[0] == 'be' and div == 'B' and whichsem == 'Even'):
                for tmng in range(7):
                    timetable[days.index(p2_days[1])][tmng].append(['', 'P2', '', '', '', '', '', 'S-', ''])

            if(y[0] == 'be' and div == 'A' and whichsem == 'Odd'):
                for tmng in range(3):
                    timetable[days.index(p2_days[0])][tmng].append(['', 'P2', '', '', '', '', '', 'S-', ''])
                for tmng in range(3, 6):
                    timetable[days.index(p2_days[1])][tmng].append(['', 'P2', '', '', '', '', '', 'S-', ''])

            elif (y[0] == 'be' and div == 'B' and whichsem == 'Odd'):
                for tmng in range(3):
                    timetable[days.index(p2_days[1])][tmng].append(['', 'P2', '', '', '', '', '', 'S-', ''])
                for tmng in range(3, 6):
                    timetable[days.index(p2_days[0])][tmng].append(['', 'P2', '', '', '', '', '', 'S-', ''])

            # set zero hour for tt => thur 4 lecture
            timetable[days.index(zero_day)][meettime[0].index(zero_time)].append(['', 'Zero Hour', '', '', '', '', '', 'S-', ''])
                # timetable[days.index(zero_days[1])][meettime[0].index(zero_time)].append(['', 'Zero Hour', '', '', '', '', '', 'S-', ''])
            toplabtime = []
            toplabs =  [[],[],[],[]]
            tp_room = random.choice(room_tp)
            count_toplabs = 0
            # set tp_lecture
            teac = tp_lecture[count_tp]
            tea_matrix[days.index(tp_day)][meettime[0].index(tp_time)].append(teac)
            room_matrix[days.index(tp_day)][meettime[0].index(tp_time)].append(tp_room)
            timetable[days.index(tp_day)][meettime[0].index(tp_time)].append(['', 'T&P', teac, '', tp_room, '', '', 'S-', ''])

            # for labs
            for i in population[1]:
                if i[0] == y[0] and i[3] == div:
                    # check for teachers conflicts
                    # map lab times and lec times
                    separatetime = getTime(i[5])
                    separatetime1, separatetime2 = separatetime[:11], separatetime[11:]
                    # print(separatetime, separatetime1, separatetime2 )
                    if len(toplabtime) <= 4:
                    # check lab room and teacher conflicts
                        if (i[-3] not in room_matrix[days.index(i[4])][meettime[0].index(separatetime1)]) and (i[-3] not in room_matrix[days.index(i[4])][meettime[0].index(separatetime2)]):
                            if (i[2] not in tea_matrix[days.index(i[4])][meettime[0].index(separatetime1)]) and (i[2] not in tea_matrix[days.index(i[4])][meettime[0].index(separatetime2)]):
                                # to check for not conflicting with zero hour
                                if not (zero_day == i[4] and zero_time == i[5]):
                                    if not (tp_day == i[4] and tp_time == i[5]):
                                        # if len(timetable[days.index(d)][meettime[0].index(m)]) == 0:
                                        if len(timetable[days.index(i[4])][meettime[0].index(separatetime1)]) == 0 and len(timetable[days.index(i[4])][meettime[0].index(separatetime2)]) == 0:
                                        # if 'p2' != timetable[days.index(i[4])][meettime[0].index(separatetime1)] and 'p2' != timetable[days.index(i[4])][meettime[0].index(separatetime2)]:
                                        # if not (i[4] in l and i[5] == '02:40-04:40'):
                                        # print(lab_matrix[days.index(i[4])][meettime[1].index(i[5])])
                                            if(lab_matrix[days.index(i[4])][meettime[1].index(i[5])]>0):
                                                if(i[4]+i[5] not in toplabtime):
                                                    if all(i[4] not in item for item in toplabtime):
                                                        if len(toplabtime) < 4:
                                                            toplabtime.append(i[4]+i[5])

            count_toplabs = 0
            for i in population[1]:
                if i[0] == y[0] and i[3] == div:
                    if i[4]+i[5] in toplabtime:
                        index1 = toplabtime.index(i[4]+i[5])
                        if len(toplabs[index1]) < 4:
                            if i not in toplabs[index1]:
                                if all(i[2] not in tealab for tealab in toplabs[index1]):
                                    # for no 2 occupied at same time
                                    if all(i[-3] not in labroom for labroom in toplabs[index1]):
                                        # check for teachers conflicts
                                        # map lab times and lec times
                                        separatetime = getTime(i[5])
                                        separatetime1, separatetime2 = separatetime[:11], separatetime[11:]
                                        # count_toplabs +=1
                                        toplabs[index1].append(i)
                                        tea_matrix[days.index(i[4])][meettime[0].index(separatetime1)].append(i[2])
                                        tea_matrix[days.index(i[4])][meettime[0].index(separatetime2)].append(i[2])
                                        room_matrix[days.index(i[4])][meettime[0].index(separatetime1)].append(i[-3])
                                        room_matrix[days.index(i[4])][meettime[0].index(separatetime2)].append(i[-3])
                                        timetable[days.index(i[4])][meettime[0].index(separatetime1)].append(i)
                                        timetable[days.index(i[4])][meettime[0].index(separatetime2)].append(i)
            for k in toplabtime:
                lab_matrix[days.index(k[:3])][meettime[1].index(k[3:])]-=1
            # for subjects

            for d in days:
                prior_i = "null"
                for m in meettime[0]:
                    for i in population[0]:
                        if i[0] == y[0] and i[3] == div:
                            if i[5] == d and i[6] == m:
                                if len(timetable[days.index(d)][meettime[0].index(m)]) == 0:
                                    # set free lecture
                                    if i[6] == meettime[0][6] and count_free < 1:
                                        count_free += 1
                                        timetable[days.index(d)][meettime[0].index(m)].append(['', 'Free Lecuture', '', '','', '', '', 'S-', ''])
                                    # check for consecutive lectures
                                    else:
                                        if prior_i != i[1]:
                                            if i[2] not in tea_matrix[days.index(d)][meettime[0].index(m)]:
                                                if i[4] not in room_matrix[days.index(d)][meettime[0].index(m)]:
                                                    timetable[days.index(d)][meettime[0].index(m)].append(i)
                                                    prior_i = i[1]
                                                    tea_matrix[days.index(d)][meettime[0].index(m)].append(i[2])
                                                    room_matrix[days.index(d)][meettime[0].index(m)].append(i[4])
            all_time.append(timetable)
    return all_time
