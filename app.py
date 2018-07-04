from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
# from data import Courses#function in data.p
from flask_mysqldb import MySQL
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_bootstrap import Bootstrap
from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
# from wtforms import widgets
# from wtforms.compat import text_type, string_types
# from wtforms.fields import SelectFieldBase
# from wtforms.validators import ValidationError
# from

# from wtforms_components import Unique
# from Flask_SQLAlchemy import ModelForm
# from flask_Salchemy import ModelForm
# from flaskext.mysql import MySQL
# from ge   t import get
# from flaskext.mysql import MySQL

app = Flask(__name__)

# config MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ttgeneration'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


# config MySQL for SQLAlchemy
# 'mysql://username:password@server/db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/ttgeneration'
#                                         # 'mysql://scott:tiger@localhost/mydatabase'
# db = SQLAlchemy(app)
#
# class Users(db.Model):
# 	__tablename__ = 'users'
# 	u_id = db.Column('t_id', db.Integer, primary_key=True)
# 	u_name = db.Column('t_name', db.String(50),unique=True)

# init MySQL
mysql= MySQL(app)
# for bootstrap
Bootstrap(app)

# @app.route('/about')
# def show_about():
#     return render_template('about.html')

listing = []
years = ['seA', 'seB', 'beA', 'beB', 'teA', 'teB']
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

    # catch Exception as e:
    #     print(str(e))

        # make list
        # for x in value1.split('~'):
        #     listy = []
        #     for y in x.split(','):
        #         listy.append(x)
        #     listing.append(listy)
        #
        # for x in value1.split('~'):
        #     listy = []
        #     for y in x.split(','):
        #         listy.append(x)
        #     teacher_list.append(listy)
        #
        # for i in range(listing):
        #     for j in listing[i]:
        #         cur.execute("INSERT INTO subtea(sub, tea, year, div) VALUES (%s, %s, %s, %s)", (j, teacher_list[0] , listy[i * 2], listy[i * 2 + 1]))
        #         mysql.connection.commit()
        #

        # for subjects name
        # for i,x in enumerate(value1.split('~')):
        #     for j,y in enumerate(x.split(',')):
        #             m = 0
        #             cur.execute("INSERT INTO subjects(s_name, year, division) VALUES (%s, %s, %s)", (y,years[i],divs[j]))
        #             mysql.connection.commit()
        #     m = 1
    #         cur.execute("INSERT INTO rooms(r_name) VALUES (%s)", (x,))
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

#
# i = '1/2/3';
# j = '4,5/6,7/8,9';
# k = '8,8/8,8/8,8';
# for i,j,k in zip(value1.split('/'),value2.split('/'),value3.split('/')):
#     for l,m,n in zip(i.split('~'),j.split('~'),k.split('~')):
#         print(l+m+n)
        # count = 0
        # cur = mysql.connection.cursor()
        # list3 = []
        # listty = []
        # count = -1
        # for x in value1.split('/'):
        #     for j in x.split('~'):
        #         for k in j.split(':'):
        #             list3.append(k)
        #     listty.append(list3)
        #
        # print(listty)
        # for x in range(len(listty)):
        #     # print(count)
        #     # print(years)
        #     firstyear = years[count]
        #     # print(firstyear
        #     cur.execute("INSERT INTO labs(l_name, l_teac, l_room, year, division) VALUES (%s, %s, %s, %s, %s)", (list3[x], list3[x + 1], list3[x + 2], firstyear[:2], firstyear[-1]))
        #     x += 3
        #     mysql.connection.commit()
        # cur.close()
        # cur.execute("INSERT INTO subjects(s_id, s_name, year, division) VALUES (%s, %s, %s, %s)", (k,l,s1,s2,))
        #     mysql.connection.commit()
        #     cur.close()
        return render_template('afterlab.html')
    else:
        return render_template('afterlab.html')

# list3 = []
# value = 'l1:t1,t2,t3:r1,r2/l2:t3,t4,t5,t1:r3,r4/l2:t3,t9,t8,t7:r5'
# count = 0
# for x in value.split('/'):
#   for j in x.split(':'):
#     list3.append(j)
#
# for x in range(len(list3)):
#   cur.execute("INSERT INTO labtea(lab, teac, room) VALUES (%s, %s, %s)", (list3[x], list3[x + 1], list3[x + 2]))
#   x += 3

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
    year = SelectField('Year', choices=[('first','First Year'),('second','Second Year'),('third','Third Year'),('final','Final Year')])
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
        redirect(url_for('show_index')) #method name for index.
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

                flash('logged in', 'success')
                return redirect(url_for('dashboard'))
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

#user log in
if __name__ ==  '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
