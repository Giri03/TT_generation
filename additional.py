# tea - teacher
from data import years,days,meettime,divs
from populations import pop

population = pop
timetable = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
lab_matrix = [[2,2,1,1],[2,2,1,1],[2,2,1,1],[2,2,1,1],[2,2,1,1]]
tea_matrix = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
# population[0].sort(key = lambda x:x[-1])
population[0].sort(key = lambda x:x[-1])
population[1].sort(key = lambda x:x[-1])

for y in years:
    for div in divs:
        y = years[0]
        div = 'A'
        timetable = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
        toplabtime = []
        toplabs =  [[],[],[],[]]
        count_toplabs = 0
        for i in population[1]:
            if i[0] == y[0] and i[3] == div:
                if(lab_matrix[days.index(i[4])][meettime[1].index(i[5])]>0):
                    if(i[5] and i[4] not in toplabtime):
                        if all([i[4] not in item for item in toplabtime]):
                            if len(toplabtime) <= len(y[2]):
                                toplabtime.append(i[4]+i[5])
                                if len(toplabtime) >= len(y[2]):
                                    break
        count_toplabs = 0
        for i in population[1]:
            if i[0] == y[0] and i[3] == div:
                if i[4]+i[5] in toplabtime:
                    index1 = toplabtime.index(i[4]+i[5])
                    if len(toplabs[index1]) < 4:
                        if i[-2] not in toplabs[index1]:
                            count_toplabs +=1
                            toplabs[index1].append(i[-2])
                            timetable[days.index(i[4])][meettime[1].index(i[5])*2].append(i[-2])
                            # for conflicts in last 2 lectures in tt
                            if(not meettime[1][-1]==i[5]):
                                timetable[days.index(i[4])][meettime[1].index(i[5])*2+1].append(i[-2])
                            else:
                                timetable[days.index(i[4])][5].append(i[-2])
                            # if count_toplabs >= 16:
                            #     break
        for k in toplabtime:
            lab_matrix[days.index(k[:3])][meettime[1].index(k[3:])]-=1
        # for subjects
        for d in days:
            for m in meettime[0]:
                for i in population[0]:
                    if i[0] == y[0] and i[3] == 'A':
                        if i[5] == d and i[6] == m:
                            if not timetable[days.index(d)][meettime[0].index(m)]:
                                if i[2] not in tea_matrix[days.index(d)][meettime[0].index(m)]:
                                    timetable[days.index(d)][meettime[0].index(m)].append(i[-2])
                                    tea_matrix[days.index(d)][meettime[0].index(m)].append(i[1])
print(tea_matrix)
for x in timetable:
    print(x)


# print(toplabs)
# print(toplabtime)
# print(lab_matrix)
# for x in timetable:
#     for y in x:
#         print(y)
