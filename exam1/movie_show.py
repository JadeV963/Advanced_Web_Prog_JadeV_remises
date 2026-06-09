from constants import MAX_TICKETS_PER_BOOKING
from show_status import ShowStatus
from exceptions import InvalidBookingError, ShowSoldOutError, ShowCancelledError


class MovieShow:
    def __init__(self, title, capacity):
        if not title.strip():
            raise ValueError("title cannot be empty")
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        self.__title = title
        self.__capacity = capacity
        self.__booked_seats = 0
        self.__status = ShowStatus.OPEN


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <=0:
            raise ValueError("capacity must be greater than 0")
        self.__capacity = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        if not isinstance(value, ShowStatus):
            raise ValueError("invalid status")
        self.__status = value

    @property
    def remaining_seats(self):
        return self.__capacity - self.__booked_seats

    def book_tickets(self, customer, quantity):
        if quantity <=0:

            raise InvalidBookingError("Quantity must be greater than 0")

        if quantity > MAX_TICKETS_PER_BOOKING:

            raise InvalidBookingError(f"Cannot book more than {MAX_TICKETS_PER_BOOKING} tickets")
        
        if self.__status == ShowStatus.CANCELLED:

            raise ShowCancelledError("This show is cancelled")

        if self.__status == ShowStatus.SOLD_OUT:

            raise ShowSoldOutError("There are no more tickets for this show")

        if quantity > self.remaining_seats:

            raise InvalidBookingError("NOT ENOUGH SEATS AVAILABLE")


        self.__booked_seats += quantity
        if self.__booked_seats ==self.__capacity:
           self.__status = ShowStatus.SOLD_OUT

        print(f"{customer.name} successfully booked {quantity} ticket(s) for {self.__title}")

    def cancel_show(self):
        self.__status = ShowStatus.CANCELLED
        print(f"{self.__title} has been cancelled")


    def display_info(self):
        print(f"Title: {self.__title}  Capacity: {self.__capacity}  Booked:{self.__booked_seats}. Remaining: {self.remaining_seats}. Status: {self.__status.value}")