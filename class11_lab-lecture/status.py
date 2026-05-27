#Step1
from enum import Enum

class CourseStatus(Enum):
    OPEN = "open"
    CLOSED ="closed"
    CANCELLED = "cancelled"

class DeliveryMode(Enum):
    ONLINE = "online"
    IN_PERSON = "in_person"
    HYBRID = "hybrid"

