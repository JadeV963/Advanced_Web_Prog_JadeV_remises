from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello to my website</h1>"
 
@app.route("/games")
def games():

    games_list = ""

    for i in range(1,4):
        games_list +=f"<li>Game {i}</li>"

    return f"<u>{games_list}</ul>"

@app.route("/students")
def students():
    return "Welcome to students page"