from flask import Flask, render_template, request, redirect
# import the class from friend.py
from flask_app import app
from flask_app.models.user import User

@app.route("/users")
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    return render_template("index.html", all_users = users)

@app.route("/users/new")
def user_form():
    # render the form 
    return render_template("create_user.html")

@app.route("/users/<int:id>")
def show_user(id):
    # call the get one class method to get one user
    user = User.get_one(id)
    return render_template("show_user.html", user = user)

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    id = User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users/'+ str(id))

@app.route('/users/<int:id>/edit')
def edit_form(id):
    #render the edit form
    user = User.get_one(id)
    return render_template("edit_user.html",user = user)


@app.route('/edit_user/<int:id>', methods=["POST"])
def edit_user(id):
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "id":  id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.edit(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users/'+ str(id))

@app.route('/delete/<int:id>', methods = ["POST"])
def delete_user(id):
    User.delete(id)
    return redirect('/users')