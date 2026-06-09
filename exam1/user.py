class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name} | Email:{self.email}")

class Customer(User):
    def __init__(self, name, email, customer_id):
        super().__init__(name, email)
        self.__customer_id = customer_id
    
    def display_info(self):
        print(f"Customer Name: {self.name} Email: {self.email}  ID: {self.__customer_id}")

class Staff(User):
    def __init__(self, name, email, employee_id):
        super().__init__(name, email)
        self.__employee_id = employee_id
    
    def display_info(self):
        print(f"Staff Name: {self.name}  Email: {self.email} Employee ID:{self.__employee_id}")

