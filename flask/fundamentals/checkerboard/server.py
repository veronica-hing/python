from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<int:width>/<int:height>')
def checkerboard(width, height):
    return render_template("index.html", width = width, height = height)

if __name__ == "__main__":
    app.run(debug = True)