# tea - teacher
from data import years,days,meettime
population = [['be', 'l42', 't17', 'A', 'wed', '09:00-11:00', 530, 4], ['be', 'l42', 't17', 'A', 'wed', '09:00-11:00', 541, 4], ['se', 'l23', 't19', 'A', 'wed', '02:40-04:40', 557, 4], ['be', 'l32', 't10', 'A', 'tue', '01:40-03:40', 559, 4], ['be', 'l41', 't16', 'A', 'mon', '11:10-1:10', 562, 4], ['be', 'l44', 't20', 'A', 'wed', '02:40-04:40', 565, 4], ['se', 'l23', 't6', 'A', 'wed', '02:40-04:40', 18, 5], ['be', 'l32', 't10', 'A', 'thu', '02:40-04:40', 31, 5], ['be', 'l44', 't20', 'A', 'wed', '02:40-04:40', 37, 5], ['be', 'l31', 't7', 'A', 'mon', '01:40-03:40', 41, 5]]
divs = ['A', 'B']
toplabtime = []
toplabs =  [[],[],[],[]]
count_toplabs = 0
timetable = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
lab_matrix = [[2,2,1,1],[2,2,1,1],[2,2,1,1],[2,2,1,1],[2,2,1,1]]
tea_matrix = [ [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]], [[],[],[],[],[],[],[]] ]
# population[0].sort(key = lambda x:x[-1])
population.sort(key = lambda x:x[-1])
for y in years:
    for div in divs:
        for i in population:
            if i[0] == y[0] and i[3] == div:
                if(lab_matrix[days.index(i[4])][meettime[1].index(i[5])]>0):
                    if(i[5] and i[4] not in toplabtime):
                        if all([i[4] not in item for item in toplabtime]):
                            if len(toplabtime) <= len(y[2]):
                                toplabtime.append(i[4]+i[5])
                                if len(toplabtime) >= len(y[2]):
                                    break
        for i in population:
            if i[0] == y[0] and i[3] == div:
                if i[4]+i[5] in toplabtime:
                    index = toplabtime.index(i[4]+i[5])
                    if len(toplabs[index]) < 4:
                        if i[-2] not in toplabs[index]:
                            count_toplabs +=1
                            toplabs[index].append(i[-2])
                            timetable[days.index(i[4])][meettime[1].index(i[5])*2].append(i[-2])
                            # for conflicts in last 2 lectures in tt
                            if(not meettime[1][-1]==i[5]):
                                timetable[days.index(i[4])][meettime[1].index(i[5])*2+1].append(i[-2])
                            else:
                                timetable[days.index(i[4])][5].append(i[-2])
                            if count_toplabs >= 12:
                                break
        for k in toplabtime:
            lab_matrix[days.index(k[:3])][meettime[1].index(k[3:])]-=1

        # for subjects
        for d in days:
            for m in meettime[0]:
                for i in population[0]:
                    if i[5] == d and i[6] == m:
                        if not timetable[days.index(d)][meettime[0].index(m)]:
<<<<<<< HEAD
                            if i[2] not in teamatrix[days.index(d)][meettime[0].index(m)]:
                                timetable[days.index(d)][meettime[0].index(m)].append(i[-2])
                                teamatrix[days.index(d)][meettime[0].index(m)].append(i[2])

=======
                            if i[2] not in teamatrix[days.index(d)][meettime[0]
>>>>>>> 681e808d5312b55001a8966530a1a586fdef0e15
print(toplabs)
print(toplabtime)
print(lab_matrix)
