@app.route('/dashboard', methods=['GET','POST'])
@is_logged_in
def dashboard():
    global population
    cur = mysql.connection.cursor()
    cur.execute("SELECT t_name FROM teachers")
    sp = cur.fetchall()
    teachers = []
    for row in sp:
        teachers.append(row['t_name'])
    cur.execute("SELECT r_name FROM rooms")
    sp = cur.fetchall()
    rooms = []
    for row in sp:
        rooms.append(row['r_name'])
    cur.execute("SELECT s_name, s_teach, year, division FROM subjects")
    sub = cur.fetchall()
    cur.execute("SELECT l_name, l_teac, l_room, year, division FROM labs")
    lab = cur.fetchall()

    se = ['se']
    te = ['te']
    be = ['be']
    divs = ['A', 'B']
    years = [se, te, be]
    for y in years:
        only_subj = []
        for i in sub:
            if i['s_name'] not in only_subj and i['year'] == y[0]:
                only_subj.append(i['s_name'])
        y.append(only_subj)
    for y in years:
        only_lab = []
        for i in lab:
            if i['l_name'] not in only_lab and i['year'] == y[0]:
                only_lab.append(i['l_name'])
        y.append(only_lab)
    ids = -1
    for j in range(population_sub_size):
        for i in sub:
            ids += 1
            population_sub.append([i['year'], i['s_name'], i['s_teach'], i['division'], random.choice(rooms), random.choice(days), random.choice(meettime[0]), 'S-'+str(ids) , -1])
    for j in range(population_lab_size):
        for i in lab:
            ids += 1
            population_lab.append([i['year'], i['l_name'], random.choice(i['l_teac'].split(',')), i['division'], random.choice(days), random.choice(meettime[1]),  random.choice(i['l_room'].split(',')), 'L-'+str(ids) , -1])
    population.append(population_sub)
    population.append(population_lab)
    mysql.connection.commit()
    cur.close()
    # print(population)
    population = fitness(population)
    population = labs_labs(population)
    population1 = tournament(population)
    population1 = crossover(population1)
    population1 = mutation(population1)
    population1 = change_fitness(population1)
    population1 = fitness(population1)
    population = new_population(population, population1)
    all_timetable = timetables(population)
    # print(all_timetable)
    if(1 <=now.month<=6):
        var = "Even"
    else:
        var =  "Odd"
    yr = now.year
    return render_template('timetable.html',vars = var, y = yr, timetable=all_timetable, index=year_index,day=dayys,year=yearss)
