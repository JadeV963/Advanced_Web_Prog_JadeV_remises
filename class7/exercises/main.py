# Let's create a Product from different formats

# you are designing a product class
    # product class needs:
        # name
        # price
        # category

# the data to create this class may arrive in 3 different formats:
    
# you need to design the class so all three formats can be used cleanly.
class Product:
    # 1. separate constructor arguments (__init__)
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    # 2. one comma-separated string
    @classmethod
    def from_string(cls, data):
        parts = data.split(",")
        name = parts[0]
        price = float(parts[1])
        category = parts[2]
        return cls(name, price, category)
    
    # 3. a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"], data["category"])
    
    # 4. a new product with no category and price (just a name)
    @classmethod
    def from_name(cls, data):
        return cls(data, 0, "")
    
    def show(self):
        print(f"{self.name} is ${self.price} and is in category: {self.category}")
    

# created with comma separated string
product1 = Product.from_string("Mouse,100,Category 1")

# created with a dictionary
product2 = Product.from_dict({"name": "Tablet", "price": 50, "category": "electronics"})

# with normal constructor
product3 = Product("Keyboard", 20, "Utils")

# with just a name
product4 = Product.from_name("Screen")

product1.show()
product2.show()
product3.show()
product4.show()