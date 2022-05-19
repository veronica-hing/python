from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def lazy():
    return redirect("/dojos")

@app.route("/dojos")
def index():
    #call classmethod to get all dojos for list of dojos
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)

@app.route("/dojos/save", methods = ["POST"])
def save():
    data = {
        "name": request.form["name"]
    }
    id = Dojo.save(data)
    #can use fstring as well f'/dojos/{id}'
    return redirect('/dojos/' + str(id))

@app.route("/dojos/<int:id>")
def show_dojo(id):
    dojo = Dojo.get_dojo_with_ninjas(id)
    return render_template("show_dojo.html", dojo = dojo)