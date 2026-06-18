class Book:
    def __init__(self, name):
        self.name = name

book1 = Book("test")
book1.name = "something else"

print(book1.name)


