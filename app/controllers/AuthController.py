from flask import render_template, request, flash
from app.models.auth import add_user, get_single_user
from app import app

app.secret_key = "jamie"


def login_page():
    return render_template('auth/login.html')



def signup():
    # To Get Signup UI
    if request.method == 'GET':
        return render_template('auth/signup.html')
    # To Process Form Submission
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        password = request.form['password']

    if len(get_single_user(email)) == 0:

        if add_user(first_name, last_name, email, password):
            flash("Sign Up Successful")
            return render_template('auth/signup.html')
        return "sign up failed for some reason"
    
    flash("User Already Exists")
    return render_template('auth/signup.html')
    


def add_to_db():
    if add_user("bishal", "giri", "giribishal09@gmail.com", 33):
        return "Database query successful"
    return "failed to add data"