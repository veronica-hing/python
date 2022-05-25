from flask import render_template, request, redirect, flash
from flask_app import app, session
from flask_app.models.user import User
from flask_app.models.cocktail import Cocktail
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    #render the cocktails slideshow
    return render_template("landing.html")

@app.route("/login")
def login():
    #render the registration and login form
    return render_template("login.html")

@app.route("/register_user", methods = ["POST"])
def register_user():
    #check if email is already registered
    if(User.get_by_email is not False):
        flash("Email is already registered, please log in")
        return redirect("/login")
    #check if user_name is already registered
    #check if inputs are valid
    if not User.validate_user(request.form):
        #redirect to reg form since user is not good
        session['failed_register'] = True
        return redirect("/login")

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
    if session.get("user") is None:
        return redirect("/")
    #render user page
    recipes = Recipe.get_all()
    return render_template("dashboard.html", recipes = recipes)

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