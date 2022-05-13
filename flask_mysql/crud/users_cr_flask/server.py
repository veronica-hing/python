from flask import Flask, render_template
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    return render_template("index.html", all_users = users)
            
if __name__ == "__main__":
    app.run(debug=True)