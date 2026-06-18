from constants import MAX_TICKETS_PER_BOOKING
from enums import ShowStatus
from customer import Customer
from movie_show import MovieShow

def main():
    customer = Customer("Ava")
    show = MovieShow("Inception", 20, ShowStatus.OPEN)

    customer.display_info()
    show.display_info()
    print("Max tickets per booking:", MAX_TICKETS_PER_BOOKING)

if __name__ == "__main__":
    main()






























