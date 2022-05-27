from flask import render_template, request, redirect, flash
from flask_app import app, session
from flask_app.models.cocktail import Cocktail
import requests

# @app.route("/cocktails/new")
# def cocktail_form():
#     #render the registration and login form
#     return render_template("cocktail_form.html")

# @app.route("/cocktails/create", methods = ["POST"])
# def cocktail_create():
#     #submit the cocktail to the server and get id
#     data = {
#         "name" : request.form["name"],
#         "description": request.form["description"],
#         "instruction": request.form["instruction"],
#         "is_quick": request.form["is_quick"],
#         "made_at": request.form["made_at"],
#         "users_id": request.form["users_id"]
#     }
#     cocktail_id = Cocktail.save(data)
#     return redirect("/cocktails/"+ str(cocktail_id))

@app.route("/cocktails/search", methods = ["POST"])
def cocktail_search():
    cocktail_name = request.form["cocktail_name"]
    #reformat the cocktail name to have '_' instead of ' '
    cocktail_name = cocktail_name.replace(" ","_")
    print(cocktail_name)
    params = {'s' : cocktail_name}
    url = "https://www.thecocktaildb.com/api/json/v1/1/search.php"
    res = requests.get(url = url, params = params)
    if res is Null:
        return redirect("/dashboard/")
    print(res)

@app.route("/cocktails/<int:id>")
def cocktail_show(id):
    #submit the cocktail to the server and get id
    data = {"id": id}
    # cocktail = Cocktail.get_one(data) #this is an obj
    # if cocktail is not False:
    #     return render_template("cocktail_details.html", cocktail = cocktail)
    # else:
    return render_template("api_cocktail_details.html")

# @app.route("/cocktails/edit/<int:id>")
# def cocktail_edit(id):
#     #render the template for edit form with the cocktail as default values
#     data = {"id": id}
#     cocktail = Cocktail.get_one(data) #this is a cocktail obj
#     return render_template("cocktail_edit.html", cocktail = cocktail)

# @app.route("/cocktails/edit/submit", methods = ["POST"])
# def cocktail_edit_submit():
#     data = {
#         "name" : request.form["name"],
#         "description": request.form["description"],
#         "instruction": request.form["instruction"],
#         "is_quick": request.form["is_quick"],
#         "made_at": request.form["made_at"],
#         "id": request.form["cocktail_id"]
#     }
#     updated = Cocktail.edit(data)
#     return redirect("/dashboard")

# @app.route("/cocktails/delete/<int:id>", methods = ["POST"])
# def cocktail_delete(id):
#     #submit the cocktail to the server and get id
#     data = {"id": id}
#     cocktail = Cocktail.delete(data) 
#     return redirect("/dashboard")