from core.enums import ShowStatus

class MovieShow:
    def __init__(self, title, capacity, status):
        self.title = title
        self.capacity = capacity
        self.status = status

    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status: {self.status.value}")
