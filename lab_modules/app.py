from constants import MAX_TICKETS_PER_BOOKING
from enums import ShowStatus
from exceptions import InvalidBookingError

class InvalidBookingError(Exception):
    pass

class Customer:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Customer: {self.name}")

class MovieShow:
    def __init__(self, title, capacity, status):
        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

if __name__ == "__main__":
    main()
































