import os

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import(
    LoginManager, 
    current_user, 
    login_required,
    login_user, 
    logout_user,
)


from models import db, User, Book, READING_STATUSES

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

#### Home route - redirects to the appropriate page
@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("books"))
    return redirect(url_for("login"))

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

        existing_username = User.query.filter_by(username=username).first()
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
    
###Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("books"))

    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash("Invalid username or password", "error")
            return render_template("login.html", username=username)

        login_user(user)

        flash("you are now logged in: ", "success")

        return redirect(url_for("books"))
        
    return render_template("login.html")

#### Logout route
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()

    flash("you have been logged out.", "success")

    return redirect(url_for("login"))



### View all books belonging to the current user

@app.route("/books")
@login_required
def books():
    user_books = Book.query.filter_by(user_id=current_user.id).all()

    return render_template("books.html", books=user_books)


### Add a new book
@app.route("/books/new", methods=["GET", "POST"])
@login_required
def new_book():
    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note =  request.form.get("note", "").strip()
        status = request.form["status"]

        errors = []

        if not title:
            errors.append("Title is required.")

        if len(title) > 100:
            errors.append("Title may contain at most 100 characters.")

        if not author:
            errors.append("Author is required.")

        if len(author) > 100:
            errors.append("Author may contain at most 100 characters.")

        if len(note) > 1000:
            errors.append("Note may contain at most 1000 characters.")

        if status not in READING_STATUSES:
            errors.append("Invalid reading status.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "book_form.html",
                title=title,
                author=author,
                note=note,
                status=status,
                statuses = READING_STATUSES,
            )

        book = Book(
            title=title,
            author=author,
            note=note,
            status=status,
            user_id=current_user.id,
        )

        db.session.add(book)
        db.session.commit()

        flash("Book added to your reading list!", "success")

        return redirect(url_for("books"))
    
    return render_template("book_form.html", statuses=READING_STATUSES)


#### Edit an existing book (title,,  author, note, status)
@app.route("/books/<int:book_id>/edit", methods=["GET", "POST"])
@login_required
def edit_book(book_id):
    book = Book.query.get_or_404(book_id)

    #Ownership check: a user may only edit their own books.
    if book.user_id != current_user.id:
        flash("You do not have permission to edit that books.", "error")
        return redirect(url_for("books"))

    if request.method == "POST":
        title = request.form["title"].strip()
        author = request.form["author"].strip()
        note = request.form.get("note", "").strip()
        status = request.form["status"].strip()

        errors = []

        if not title:
            errors.append("Tilte is required.")

        if len(title) > 100:
            errors.append("Title may contain at most 100 characters.")

        if not author:
            errors.append("Author is required.")

        if len(author) > 100:
            errors.append("Author may contain at most 100 characters.")

        if status not in READING_STATUSES:
            errors.append("Invalid reading status.")

        if errors:
            for error in errors:
                flash(error, "error")
            return render_template(
                "book_edit.html", book=book, statuses=READING_STATUSES
            )
        book.title =title
        book.author = author
        book.note = note
        book.status = status

        db.session.commit()

        flash("Book updated!", "success")

        return redirect(url_for("books"))

    return render_template("book_edit.html", book=book, statuses=READING_STATUSES)


### DElete a book
@app.route("/books/<int:book_id>/delete", methods=["POST"])
@login_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)

    #A user may only delete their own books.
    if book.user_id != current_user.id:
        flash("You do not have the permission to delete that book.", "error")
        return redirect(url_for("books"))
    
    db.session.delete(book)
    db.session.commit()

    flash("Book deleted.", "success")

    return redirect(url_for("books"))


if __name__ == "__main__":
    app.run(debug=True, port=5001)