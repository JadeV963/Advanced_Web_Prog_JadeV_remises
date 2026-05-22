class StudentRecord:
    def __init__(self, name, gpa, credits):
        self.name = name
        self.gpa = gpa
        self.credits = credits

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if value >= 0.0 and value < 4.0:
            self.__gpa = value
        else:
            print("must be between 0 and 4")

    @property
    def credits(self):
        return self.__credits
          
    @credits.setter
    def credits(self, value):
        if value >= 0:
            self.__credits = value
        else:
            print(f"must be more than 0")

    def display_info(self):
        print(f"Student infos are: {self.name}, {self.__gpa}, {self.__credits}")
        
    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount

    def update_gpa(self, value):
        self.gpa = value

class CourseSection:
    def __init__(self, title, capacity, enrolled = 0):
        self.title = title
        self.__capacity = capacity
        self.__enrolled = enrolled

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value > 0:
            self.__capacity = value
        else:
            print(f"must be sup at 0")
    
    @ property
    def enrolled(self):
        return self.__enrolled

    @enrolled.setter
    def enrolled(self, value):
        if value >= 0 and value < self.__capacity:
            self.__enrolled = value

        else:
            print(f"must be between 0 and  capacity")
            
    def register_student(self):
        if self.__enrolled < self.__capacity:
            self.__enrolled += 1
        else:
            print(f"Course is full")

    def drop_student(self):
        if self.__enrolled > 0:
            self.__enrolled -= 1
        else:
            print("there are not enough student to do that")

    def display_info(self):
        print(f"the course {self.title}, can have {self.capacity}, and have now {self.enrolled} enrolled students")


studentrec1 = StudentRecord("John", 3.2, 7)
courseSect1 = CourseSection("Webdev", 30, 7)

studentrec1.display_info()
courseSect1.register_student()
courseSect1.display_info()
studentrec1.add_credits(3)
studentrec1.display_info()

studentrec1 = StudentRecord("John", 6, 7)