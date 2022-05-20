from flask import Blueprint, request, flash, session, render_template, redirect
from dbcontrol.control import db

page = Blueprint('main-page', __name__)

@page.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':

        login = request.form.get('login')
        pwd = request.form.get('pwd')

        if login == "" or " " in login:
            flash('Error! Incorrect login format.')

        if request.form.get('registerbtn') is not None:
            isRegistered = db.registerNewUser(login, pwd) # add to db
            if not isRegistered:
                flash('Error! Username already used.')
            else:
                print(f"New user: {request.form.get('login')} | {request.form.get('pwd')}")

        elif request.form.get('loginbtn') is not None:
            userInfo = db.getUserByUsername(login)

            if userInfo is not None:
                if userInfo[2] == pwd:
                    print(f"User login: {request.form.get('login')} | {request.form.get('pwd')}")
                    session['user_id'] = userInfo[0]
                    session['username'] = userInfo[1]
                    return redirect('/dashboard')
                else:
                    flash("Error! Incorrect password. Try again...")
            else:
                flash("Error! User not found. Register please...")



    return render_template('homepage.html')