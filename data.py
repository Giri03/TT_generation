from collections import Counter
import random

# course [name, no_students, instructors]


c1 = ['c1', 25, ['James', 'Mike']]
c2 = ['c2', 35, ['James', 'Mike', 'Steve']]
c3 = ['c3', 25, ['James', 'Mike']]
c4 = ['c4', 30, ['Jane', 'Steve']]
c5 = ['c5', 35, ['Jane']]
c6 = ['c6', 45, ['James', 'Steve']]
c7 = ['c7', 45, ['Jane', 'Mike']]

course = [c1, c2, c3, c4, c5, c6, c7]

# rooms  [id, capacity]
r1 = ['r1', 25]
r2 = ['r2', 45]
r3 = ['r3', 35]

rooms = [r1, r2, r3]

# instructor [id, name]
i1 = ['i1', 'James']
i2 = ['i2', 'Mike']
i3 = ['i3', 'Steve']
i4 = ['i4', 'Jane']

instructor = [i1, i2, i3, i4]

# meetingtime [id, time]
# m1 = ['m1', '9am-10am']
# m2 = ['m2', '10am-11am']
# m3 = ['m3', '11am-12pm']
# m4 = ['m4', '12pm-1pm']

meettime = ['m1', 'm2', 'm3', 'm4']

# departments
math = [c1, c3]
ee = [c2, c4, c5]
phy = [c6, c7]

dept = [math, ee, phy]
data = [dept, instructor, course, rooms, meettime]
days = ['mon', 'tues', 'wed', 'thur', 'fri']


# creating population

schedule = []
population = []
timeslot_group = []

l = 0
population_size = 200
for j in range(population_size):
    for i in course:
        population.append([l , i[0], random.choice(i[2]), random.choice(days), random.choice(meettime), 0])
        l = l + 1

# find fitness value  or no. of conflicts      
count = 0
for i in days:
    for j in meettime:
        cou = Counter(population[s][2] for s in range(len(population)) if population[s][4] == j and population[s][3] == i )

# extracting from counter dictionary                  
for i in population:
    for j,k in cou.items():
        if j == i[2]:
            i[5] = k 


def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# crossover is 
pc = 0.7
# here selection is list obtained after tournament selection
for i in range(0, 200, 2):
    if random.random() > pc:
        if(random.choice([True, False])):
            swap(selection[i][4], selection[i+1][4])
        if(random.choice([True, False])):
            swap(selection[i][5], selection[i+1][5])

# mutation
pm = 0.2
for i in range(0, 200, 2):
    if random.random() < pm:
        if(random.choice([True, False])):
            swap(selection[i][4], random.choice(days))
        if(random.choice([True, False])):
            swap(selection[i][5], random.choice(meettime))

# create new population .. here range for new population should be 25% of original ..so 200 from crossover and mutation + 150
for i in range(150):
    selection.append(random.choice(population))
population = selection
    

# population.sort(key = lambda x: x[5] , reverse = True)
# print(population)         

            

            
                         
#    return [k for k, v in Counter(l).items() if v > 1]

        # population.append([course[i][0]])
    
#     course_name = random.choice(random.choice(dept))
#     for x in course:
#         if (x[0] == course_name):
#             instructor_name = random.choice(x[2])
#             no_students = x[1] 
#     room = random.choice(rooms)
#     meetingtime = random.choice(meettime)
#     k = [course_name, instructor_name, no_students, room[0], room[1], meetingtime[1] ]
#     schedule.append(k)

# print (schedule)
