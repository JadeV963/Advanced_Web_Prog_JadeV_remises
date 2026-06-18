from enum import Enum

class StudentLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"

class Student:
    def __init__(self, name, level):
        self.name = name
        self.level =level

    @property
    def level(self):
        return self.level
    
    @level.setter
    def level(self, value):
        if not isinstance(value, StudentLevel):
            raise ValueError("level must be a StudetnLevel value")
        self.__level = value
    def display_info(self):
        print(f"{self.name} | Level: {self.level.value}")