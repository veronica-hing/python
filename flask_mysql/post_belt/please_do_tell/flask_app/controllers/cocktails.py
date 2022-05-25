from flask import render_template, request, redirect, flash
from flask_app import app, session
from flask_app.models.cocktail import Cocktail

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