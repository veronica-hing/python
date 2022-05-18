from flask import render_template, request, redirect, flash
from flask_app import app, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    #render the registration and login form
    return render_template("index.html")

@app.route("/register_user", methods = ["POST"])
def register_user():
    if not User.validate_user(request.form):
        #redirect to reg form since user is not good
        session['failed_register'] = True
        return redirect("/")

    password = bcrypt.generate_password_hash(request.form["hashed_pw"])
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "hashed_pw": password
    }
    user_id = User.save(data)
    user = User.get_by_email({"email": request.form["email"]}) #this gives us a dictionary
    session['user'] = user
    return redirect("/dashboard/")

@app.route("/dashboard/")
def show_user():
    #render user page
    return render_template("logged_in.html")

@app.route("/login_user", methods = ["POST"])
def login_user():
    #render the registration and login form
    data = { "email": request.form["email"] }
    user = User.get_by_email(data) #this gives us a dictionary
    
    if not User.validate_login(data["email"]):
        session['failed_login'] = True
        #the method flashes if not valid
        return redirect("/")
        
    if not bcrypt.check_password_hash(user["hashed_pw"], request.form["hashed_pw"]):
        session['failed_login'] = True
        flash("Invalid Password")
        return redirect("/")

    session['user'] = user
    return redirect("/dashboard/")

@app.route("/logout")
def logout_user():
    #clear user from session
    session.clear()
    return redirect("/")