from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
    return 'Hello World!'

@app.route('/')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_name(name):
    return "Hi " + name + "!"

@app.route('/repeat/<int:nummy>/<stringy>')
def repeat_stringy(nummy, stringy):
    block = ""
    for i in range(0,nummy):
        block += f"{stringy}\n"
    return f"{block}"
if __name__ == "__main__":
    app.run(debug = True)