from data import *
# crossover is
pc = 0.7
# here selection is list obtained after tournament selection
for i in range(0, 200, 2):
    if random.random() > pc:
        if(random.choice([True, False])):
            swap(selection[i][4], selection[i+1][4])
        if(random.choice([True, False])):
            swap(selection[i][5], selection[i+1][5])
