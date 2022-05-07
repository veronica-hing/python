from flask import Flask, render_template, redirect, request, session
import json

app = Flask(__name__)
app.secret_key = "temp_key"

@app.route('/')
def index():
    #session['first_name'] = {}
    return render_template("index.html")


@app.route('/results')
def results():
    person = json.loads(session['first_name'])
    return render_template("results.html",person = person)

@app.route('/save_user', methods = ['POST'])
def save_user():
    person = {}
    for key in request.form:
        person[key.replace('_',' ').capitalize()] = request.form[key].replace('_',' ').capitalize()

    session['first_name'] = json.dumps(person)
    print(session)
    return redirect('/results')
if __name__ == "__main__":
    app.run(debug = True)
