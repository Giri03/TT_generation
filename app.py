from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Courses#function in data.p
from flask_mysqldb import MySQL
from wtforms import Form, StringField, SelectField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps
from flask_bootstrap import Bootstrap
from flask import Flask
from flask import request
from flask import render_template
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

# init MySQL
mysql= MySQL(app)
Bootstrap(app)

Courses = Courses()

# @app.route('/about')
# def show_about():
#     return render_template('about.html')

@app.route('/teacher', methods=['GET', 'POST'])
def show_teacher():
    value = request.form['allRooms']
    # value1 = request.form['labale']
    # value = "fj"
    return '<h1>'+value+'</h1>'

@app.route('/room', methods=['GET', 'POST'])
def show_room():
    return render_template('rooms.html')

# @app.route('/subject')
# def show_subject():
#     value = request.form('allTeach')
#     return '<h1>'+value+'</h1>'
    # return render_template('subject.html')

    # return render_template('subject.html')
@app.route('/lab', methods=['GET', 'POST'])
def show_lab():
    value = request.form('someS')
    return '<h1>'+value+'</h1>'

#
# @app.route('/your')
# def show_your():
#     return render_template('side_bar.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
#reg form class
class RegisterForm(Form):
    # SelectField(u'Field name', choices = myChoices, validators = [Required()])
    # unique to that column
    username = StringField('Username', [
    validators.Length(min=4, max=25),
    # validators.Unique(ttgeneration.username)
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
