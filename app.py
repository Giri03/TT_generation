from flask import Flask, make_response, render_template, flash, redirect, url_for, session, logging, request
from flask_mysqldb import MySQL
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_bootstrap import Bootstrap
from main import *
# import pdfkit

app = Flask(__name__)

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ttgeneration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# init MySQL
mysql= MySQL(app)
# for bootstrap
Bootstrap(app)
# Timetables = timetables()

# @app.route('/about')
# def show_about():
#     return render_template('about.html')

listing = []
years = ['seA', 'seB', 'teA', 'teB', 'beA', 'beB']
# divs = [a, b]
# teachers
@app.route('/teacher', methods=['GET', 'POST'])
def show_teacher():
    return render_template('teacher.html')

# rooms
@app.route('/room', methods=['GET', 'POST'])
def show_room():
    if request.method == 'POST':
        value1 = request.form['textAreaField1']
        value1 = value1.rstrip(',')
        cur = mysql.connection.cursor()
        for j in value1.split(','):
            cur.execute("INSERT INTO teachers(t_name) VALUES (%s)",(j,))
            mysql.connection.commit()
        cur.close()
        return render_template('rooms.html')
    else:
        return render_template('rooms.html')

@app.route('/subject',methods=['GET', 'POST'])
def show_subject():
    if request.method == 'POST':
        value1 = request.form['room_textAreaField']
        value1 = value1.rstrip(',')
        cur = mysql.connection.cursor()
        for j in value1.split(','):
            cur.execute("INSERT INTO rooms(r_name) VALUES (%s)",(j,))
            mysql.connection.commit()
        cur.close()
        return render_template('subject.html')
    else:
        cursor = mysql.connection.cursor()
        cur = cursor.execute("SELECT t_name FROM teachers")
        return render_template('subject.html', subject0=cursor.fetchall())

@app.route('/lab', methods=['GET', 'POST'])
def show_lab():
    if request.method == 'POST':
        value1 = request.form['Sub_textAreaField1']
        value2 = request.form['Sub_textAreaField2']
        value1 = value1.rstrip(',')
        value2 = value2.rstrip(',')
        cur = mysql.connection.cursor()
        count = 0
        for i,j in zip(value1.split('~'),value2.split('~')):
            for k,l in zip(i.split(','),j.split(',')):
                s1 = years[count][:2]
                s2 = years[count][2:]
                cur.execute("INSERT INTO subjects(s_name, s_teach, year, division) VALUES (%s, %s, %s, %s)", (k,l,s1,s2,))
                mysql.connection.commit()
            count = count + 1;
        cur.close()
        cursor = mysql.connection.cursor()
        cur = cursor.execute("SELECT t_name FROM teachers")
        return render_template('lab.html', subject0=cursor.fetchall())
    else:
        cursor = mysql.connection.cursor()
        cur = cursor.execute("SELECT t_name FROM teachers")
        return render_template('lab.html', subject0=cursor.fetchall())

@app.route('/afterlab', methods=['GET', 'POST'])
def show_afterlab():
    if request.method == 'POST':
        value1 = request.form['Lab_textAreaField']
        value2 = request.form['Lab_textAreaField2']
        value3 = request.form['Lab_textAreaField3']
        value1 = value1.rstrip('/')
        value2 = value2.rstrip('/')
        value3 = value3.rstrip('/')
        cur = mysql.connection.cursor()
        count = 0
        for i,j,k in zip(value1.split('/'),value2.split('/'),value3.split('/')):
            for l,m,n in zip(i.split('~'),j.split('~'),k.split('~')):
                s1 = years[count][:2]
                s2 = years[count][2:]
                print(l + ' ' + m +' ' +n)
                cur.execute("INSERT INTO labs(l_name, l_teac, l_room, year, division) VALUES (%s, %s, %s, %s, %s)", (l,m,n,s1,s2,))
                mysql.connection.commit()
            count = count + 1
        cur.close()

        return render_template('afterlab.html')
    else:
        return render_template('afterlab.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

#reg form class
class RegisterForm(Form):
    # SelectField(u'Field name', choices = myChoices, validators = [Required()])
    # unique to that column
    username = StringField('Username', [
    validators.Length(min=4, max=25)

    # validators.Unique(Teachers.username)
    ])
    firstname = StringField('First Name', [validators.Length(min=1, max=25)])
    lastname = StringField('Last Name', [validators.Length(min=1, max=25)])
    email = StringField('Email', [
    validators.Length(min=6, max=50),
    validators.Regexp('(\w)+@+(somaiya.edu)', message="Invalid Email Address"),
    ])
    branch = SelectField('Branch', choices=[('Electronics', 'Electronics and Telecommunication'), ('Computers', 'CS and IT')])
    year = SelectField('Year', choices=[('fe','First Year'),('se','Second Year'),('te','Third Year'),('be','Final Year')])
    division = SelectField('Division', choices=[('A','A'),('B','B')])
    password = PasswordField('Password', [
        validators.Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}', message="Password must contain special character, digit, upper case, lower case character minimum 8 digits"),

        validators.DataRequired(),
        # validators.
        validators.EqualTo('confirm', message='Password do not match')
    ])
    confirm = PasswordField('Confirm Password')

#user register
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            firstname = form.firstname.data
            email = form.email.data
            username = form.username.data
            lastname = form.lastname.data
            branch = form.branch.data
            year = form.year.data
            division = form.division.data
            password = sha256_crypt.encrypt(str(form.password.data))
            # use cursor to execute commands
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(username, firstname, lastname, email, password, year, division, branch) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (username, firstname, lastname, email, password, year, division, branch))
            #commit to db
            mysql.connection.commit()
            #close connection
            cur.close()
            # flash("your message", "type of message ")
            flash('You Are Now Registered', 'success')
            redirect(url_for('dashboard')) #method name for index.
        return render_template('register.html', form=form)

    except Exception as e:
        flash('Sorry, User name is taken!', 'danger')
        return render_template('register.html', form=form)

#userlogin
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        #get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        #create cursor
        cur = mysql.connection.cursor()

        #get user by Username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            #get stored hash
            data = cur.fetchone()
            password = data['password']

            #compare the password
            if sha256_crypt.verify(password_candidate, password):
                #session
                session['logged_in'] = True
                session['username'] = username

                year = data['year']
                division = data['division']
                year_div = year+division
                year_index = years.index(year_div)

                flash('logged in', 'success')

                return redirect(url_for('timetableId',timetable = all_timetable,index = year_index))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
    return render_template('login.html')

@app.route('/login_admin', methods=['GET','POST'])
def login_admin():
    if request.method == 'POST':
        #get form fields
        username = request.form['username']
        password_candidate = request.form['password']

        #create cursor
        cur = mysql.connection.cursor()

        #get user by Username
        result = cur.execute("SELECT * FROM admins WHERE a_name = %s", [username])
        flash(result, 'success')
        if result > 0:
            #get stored hash
            data = cur.fetchone()
            rows = data['a_password']
            if(rows == password_candidate):
            #compare the password
            # if sha256_crypt.verify(password_candidate, password):
                #session
                session['logged_in'] = True
                session['username'] = username

                flash('logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login_admin.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login_admin.html', error=error)
    return render_template('login_admin.html')

#check if user has logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login', 'danger')
            return redirect(url_for('login'))
    return wrap

@app.route('/timetableId')
def timetableId():
    return render_template('timetableId.html',timetable = all_timetable,index = 1)
#logout
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out !!', 'success')
    return redirect(url_for('login'))

#dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    return render_template('dashboard.html')

@app.route('/ttgeneration')
def show_timetable():
    # return all_timetable
    return render_template('timetable.html',timetable = all_timetable)

#user log in
if __name__ ==  '__main__':
    population = create_population()
    population = fitness(population)
    population = labs_labs(population)
    population1 = tournament(population)
    population1 = crossover(population1)
    population1 = mutation(population1)
    population1 = change_fitness(population1)
    population1 = fitness(population1)
    population = new_population(population, population1)
    all_timetable = timetables(population)
    app.secret_key='secret123'
    app.run(debug=True)
