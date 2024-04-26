#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

# class Recatangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)


# rect = Recatangle(5, 10)
# print(rect.area())

# #2. Create a BankAccount class with attributes account_number and balance. 
# #Add methods to deposit and withdraw money from the account. 

# class BankAccount:
#     def __init__(self, balance=0):
#                 self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount} into account {self.account_number}. New balance: {self.balance}")
#         else:
#             print("Invalid deposit amount. Please enter a positive number.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds")


#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

class Car:
    def __init__(self, make, model, year): #sets the arguments required
          self.make = make
          self.model = model # mapping the object with arguments
          self.year = year

    def get_make(self): # (self) = passing the object
         return self.make
    def get_model(self):
         return self.model
    def get_age(self):
         return self.year
    
    def set_make(self, make): 
         self.make = make
    def set_model(self, model):
         self.model = model
    def set_year(self, year):
         self.year = year
    
    def __str__(self):
         return f"{self.make}, {self.model}, {self.year}"
    
car1 = Car("vw", "passat", "2008")
print(car1.get_make())
car1.set_make("BMW")
car1.set_model("3 Series")
car1.set_year(2001)

print(car1)
        



#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 

class Product:
    def __init__(self, name, price, quantity):
          self.name = name
          self.price = price
          self.quantity = quantity

    def value(self):
         print(self.price * self.quantity) 
    
    def add_product(self, name):
         self.name = name
    def add_price(self, price):
         self.price = price
    def add_quantity(self, quantity):
         self.quantity = quantity

    def __str__(self):
         return f"{self.name}, {self.price}, {self.quantity}"

value = Product("beans", "0.99", "5")
print(value.get_name())
print(value)
value.set_make("BMW")
value.set_model("3 Series")
value.set_year(2001)

print(car1)
    

#Harder challenge (stretch goal): 

#Create a Book class and BookShelf class that can be used to manage a collection of books. 
#Create a Book class that has the following attributes: 
#title (str), author (str), publisher (str), publication year (int). 
#The class should also have a str method that returns the book's information in a 
#formatted string. 
#Create a BookShelf class that has the following attributes: 
#capacity (int), list of books (list). 
#The class should have the following methods: 
#- add_book: adds a book to the list of books if the shelf is not full 
#- remove_book: removes a book from the list of books if it exists on the shelf 
#- find_book_by_title: searches for a book by its title 
#and returns the book object if found 
#- find_books_by_author: searches for books by a specific author 
#and returns a list of book objects if found 
#The class should also have a str method that returns a string representation 
#of the books on the shelf. 

#Create four Book objects and add them to a BookShelf object with a capacity of three. 
#Test the BookShelf object by adding, removing, and finding books by title and author.
#Print the BookShelf object after each action.



#Alternative stretch goal: rewrite the rock/paper/scissor app using a class. 