class StudentRecord:
    def __init__(self, name, gpa, credits):
        self.name = name
        self.__gpa = gpa
        self.__credits = credits

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
            print("must be more than 0")

    def display_info(self):
        print(f"Student infos are: {self.name}, {self.__gpa}, {self.__credits}")
        
    def add_credits(self, amount):
        if amount > 0:
            self.__credits += amount

    def update_gpa(self, value):
        self.gpa = value