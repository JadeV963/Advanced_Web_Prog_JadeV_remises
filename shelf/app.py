import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import(
    LoginManager, 
    current_user, 
    login_required,
    login_user, 
    logout_user,
)


from models import db, User
app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shelf.db"

#Flask uses the secret key to securely sign session information and flash messages.
#Without it, login sessions and flash messages cannot function properly.

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")


db.init_app(app)


#login

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

with app.app_context():
    db.create_all()

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

### Registration route
@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("books"))
    if request.method == "POST":
        username = request.form["username"].strip()
        email = request.form["email"].strip().lower()
        password = request.form["password"]

        errors = []

        if not username:
            errors.append("username is required.")

            existing_username = user.query.filter_by(username=username).first()
            if existing_username:
                errors.append("That username is already in use!")

            existing_email = User.query.filter_by(email=email).first()
            if existing_email:
                errors.append("That email is already registered.")

            if not password:
                errors.append("Password is required.")

            if errors:
                for error in errors:
                    flash(error, "error")
                return render_template("register.html", username=username, email=email)

            user = User(username=username, email=email)
            user.set_password(password)

            db.session.add(user)
            db.session.commit()


            flash("Your account has been created!", "success")

            return redirect(url_for("login"))
        
        return render_template("register.html")