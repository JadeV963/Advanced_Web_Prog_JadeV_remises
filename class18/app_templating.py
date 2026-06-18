from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.htlm", title="Welcome", message="hello folks")

@app.route("/games")
def game():
    games_list = ["Street fighter", "tetris", "Pac-Man"]

    retunr render_template("game.html", games=games_list)

    @app.route("/greet")
    def greet():
        name = request.args.get("name", "Gest")
        return f"<h1>Hello, {name} </h1>"
    
    @app.rout("/Welcome")
    def welcome():
        name = request.args.get("name","Guest")
        program = request.args.get("program", 'Unknown')
        return f"<h1> {name} studies in the {program} program.</h1>"