from datetime import datetime, timezone

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()



STATUS_WANT_TO_READ = "Want to read"
STATUS_READING = "Reading"
STATUS_FINISHED = "Finished"

READING_STATUSES = [STATUS_WANT_TO_READ, STATUS_READING, STATUS_FINISHED]

class User(UserMixin, db.Model):
    __tablename__="user"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), nullable=False, unique=True)

    email = db.Column(db.String(255), nullable=False, unique=True)

    password_hash = db.Column(db.String(255), nullable=False)

    books = db.relationship("Book", backref="owner", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"

class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    author = db.Column(db.String(100), nullable=False)

    note = db.Column(db.String(1000), nullable=True)

    status = db.Column(db.String(20), nullable=False, default=STATUS_WANT_TO_READ)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    #Foreign key linking each book to the user who owns it.

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"<Book {self.id}: {self.title}>"

