# import random
# print(random.choice(['a', 'v']))


# def fitness(population):
#     count = 0
#     for i in days:
#         for j in meettime:
#             cou = Counter(population[s][2] for s in range(len(population)) if population[s][4] == j and population[s][3] == i )

#     # extracting from counter dictionary                  
#     for i in population:
#         for j,k in cou.items():
#             if j == i[2]:
#                 i[5] = k 
#     return population

from itertools import groupby
a = [[1,1,1] , [1,2,2], [1,2,3], [1,4,5]]
b = [[1,1,1] , [1,2,2], [1,2,3], [1,4,5], [1,1,1] , [1,2,2], [1,2,3], [1,4,5]]
c = a + b
print(c)

giri  = [[4, 5]]
print (list(i for i in giri[0]))

p = { 'a' : 7, 'n' : 9 }
for key, value in p.items():
    print( key + ':' + str(value))

data = [[1, 2], [4, 6]]
c = list(i for  not in data)

p = '9'
s = '0'
print(int(p+s) + 6)


d1 = '9'
d3 = '6'
d1, d3 = d3, d1
print(d1 + ' ' + d3)