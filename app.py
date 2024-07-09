from flask import Flask,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_wtf.csrf import CSRFProtect

app=Flask(__name__)
app.config['SECRET_KEY'] = 'medapp'
csrf = CSRFProtect(app)

@app.route('/')
def home_page():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login',methods=['GET','POST'])
def login_page():

    return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def sign_up():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

from forms import CheckupForm
@app.route('/checkup',methods=['GET'])
def check_up():
    myform=CheckupForm()
    # if form.validate_on_submit():
        # return redirect("report.html")
    return render_template('checkup.html',form=myform)



if __name__=="__main__":
    app.run(debug=True)