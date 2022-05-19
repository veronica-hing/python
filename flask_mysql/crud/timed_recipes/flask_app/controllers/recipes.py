from flask import render_template, request, redirect, flash
from flask_app import app, session
from flask_app.models.recipe import Recipe

@app.route("/recipes/new")
def recipe_form():
    #render the registration and login form
    return render_template("recipe_form.html")

@app.route("/recipes/create", methods = ["POST"])
def recipe_create():
    #submit the recipe to the server and get id
    data = {
        "name" : request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "is_quick": request.form["is_quick"],
        "made_at": request.form["made_at"],
        "users_id": request.form["users_id"]
    }
    recipe_id = Recipe.save(data)
    return redirect("/recipes/"+ str(recipe_id))

@app.route("/recipes/<int:id>")
def recipe_show(id):
    #submit the recipe to the server and get id
    data = {"id": id}
    recipe = Recipe.get_one(data) #this is an obj
    return render_template("recipe_details.html", recipe = recipe)

@app.route("/recipes/edit/<int:id>")
def recipe_edit(id):
    #render the template for edit form with the recipe as default values
    data = {"id": id}
    recipe = Recipe.get_one(data) #this is a recipe obj
    return render_template("recipe_edit.html", recipe = recipe)

@app.route("/recipes/edit/submit", methods = ["POST"])
def recipe_edit_submit():
    data = {
        "name" : request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "is_quick": request.form["is_quick"],
        "made_at": request.form["made_at"],
        "id": request.form["recipe_id"]
    }
    updated = Recipe.edit(data)
    return redirect("/dashboard")

@app.route("/recipes/delete/<int:id>", methods = ["POST"])
def recipe_delete(id):
    #submit the recipe to the server and get id
    data = {"id": id}
    recipe = Recipe.delete(data) 
    return redirect("/dashboard")