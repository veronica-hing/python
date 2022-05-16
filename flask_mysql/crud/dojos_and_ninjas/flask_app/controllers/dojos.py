from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/dojos")
def index():
    #call classmethod to get all dojos for list of dojos
    dojos = Dojo.get_all()
    return render_template("index.html", dojos = dojos)