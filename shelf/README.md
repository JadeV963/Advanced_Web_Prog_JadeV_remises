# Shelf

 Personal reading-list application
 Registered users can create an acocunt, and keep track of the books the want to read, are reading, or have finished reading.

 ## Features

 -user registration with a unique username and email address

 -secure password storage using password hashing( Werkzeug)

 -Login and logout
 -Each logged-in user can:
    -view reading list
    -add a book
    -edit one of their books
    -delete one of their books

-Navigation changes depending on whether the user is logged in
-Flash messages confirm actions.

## Tech stack

-Flask
-Flask-SQLALchemy
-Flask-Login
-Jinja templates
-SQLite

the app runs at `http://127.0.0.1:5001`.

## Note

every book-related route checks that the book belongs to the logged-in user before allowing an edit or delete. ownership is always set from the logged-in user when a book is created.


