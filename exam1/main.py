from user import Customer, Staff
from movie_show import MovieShow
from exceptions import InvalidBookingError, ShowSoldOutError, ShowCancelledError

#testing creation of objects

customer1 = Customer("Alice", "alice@gmail.com", "C001")
customer2 = Customer("Bob", "bob@email.com", "COO2")
staff = Staff("Elise", "john@hotmail.com", "E001")

show = MovieShow("Jurassic Park", 10)
show.display_info()

print("---")

show = MovieShow("Kimetsu No Yaiba", 10)
show.display_info()

print("---")

#valides
show.book_tickets(customer1, 3)
show.book_tickets(customer2, 2)
show.display_info()

print("---")

#invalides

try:
    show.book_tickets(customer1, 10)
except InvalidBookingError as error:
    print("InvalidBookingError:", error)

try:
    show.book_tickets(customer1, 0)
except InvalidBookingError as error:
    print("INvalidBookingError:", error)

try: 
    show2 = MovieShow("", 10)
except ValueError as error:
    print("ValueError:", error)

try: 
    show2 = MovieShow("test", -5)
except ValueError as error:
    print("valueError:, " , error)

try:
    show.cancel_show()
    show.book_tickets(customer1, 1)
except ShowCancelledError as error:
    print("ShowCancelledError", error)

print("----")

# show becoming sold out
show3 = MovieShow("Avatar", 3)
try:
    show3.book_tickets(customer1, 3)
    show3.book_tickets(customer2, 1)
except ShowSoldOutError as error:
    print("ShowSoldOutError:", error)




