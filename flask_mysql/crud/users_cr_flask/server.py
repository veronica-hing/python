from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("index.html", all_users = users)

@app.route("/users/new")
def user_form():
    # render the form 
    return render_template("create_user.html")

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
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)