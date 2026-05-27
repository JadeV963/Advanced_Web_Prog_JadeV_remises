#Step2
from status import CourseStatus, DeliveryMode

MAX_CAPACITY = 60

class Course:
     
    def __init__(self, title, capacity, status, delivery_mode):
        if capacity <= 0 or capacity > MAX_CAPACITY:
            raise ValueError(f"capacity must be between 1 and {MAX_CAPACITY}")
        self.title = title
        self.capacity = capacity
        self.status = status
        self.delivery_mode = delivery_mode

    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        if not isinstance(value, CourseStatus):
            raise ValueError("status must be a CourseStatus value")
        self.__status = value

    @property
    def delivery_mode(self):
        return self.__delivery_mode
    
    @delivery_mode.setter
    def delivery_mode(self, value):
        if not isinstance(value, DeliveryMode):
            raise ValueError("delivery_mode must be a DeliveryMode value")
        self.__delivery_mode = value


    def display_info(self):
        print(f"{self.title} | Capacity: {self.capacity} | Status:{self.status.value} | Delivery:{self.delivery_mode.value}")

    def close_registration(self):
        self.status = CourseStatus.CLOSED

    def cancel_course(self):
        self.status = CourseStatus.CANCELLED

    def reopen_course(self):
        self.status = CourseStatus.OPEN