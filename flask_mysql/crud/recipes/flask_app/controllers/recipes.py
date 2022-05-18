from flask import render_template, request, redirect, flash
from flask_app import app, session
from flask_app.models.user import User
from flask_app.models.recipe import Recipe


@app.route("/recipes/new")
def new_recipe():
    #render the registration and login form
    return render_template("new_recipe.html")

@app.route("/recipes/save", methods = ["POST"])
def save_recipe():
    #save the recipe to db
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "is_quick": request.form["is_quick"],
        "made_at": request.form["made_at"],
        "users_id": request.form["users_id"]
    }
    print(data)
    recipe_id = Recipe.save(data)
    return redirect("/dashboard/")

@app.route("/recipes/<int:id>")
def view_recipe(id):
    #render the registration and login form
    recipe = Recipe.get_by_id(id)#we've received a dictionary representing the recipe object
    return render_template("view_recipe.html", recipe = recipe)