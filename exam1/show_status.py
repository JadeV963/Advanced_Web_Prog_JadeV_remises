from enum import Enum 
#possible status of a movie show

class ShowStatus(Enum):
    OPEN = "open"
    SOLD_OUT = "sold_out"
    CANCELLED = "cancelled"