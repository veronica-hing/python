from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def new_ninjas():
    #call classmethod to get all dojos for list of dojos that the ninjas can be in
    dojos = Dojo.get_all()
    #render form with list of dojos
    return render_template("new_ninja.html", dojos = dojos)

@app.route("/create_ninja", methods = ["POST"])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    ninja_id = Ninja.save(data)
    return redirect('/dojos/'+ str(request.form["dojo_id"]))