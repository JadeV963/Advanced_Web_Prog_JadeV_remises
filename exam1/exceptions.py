#exceptions for the movie booking systm.

class InvalidBookingError(Exception):
    pass

class ShowSoldOutError(Exception):
    pass

class ShowCancelledError(Exception):
    pass