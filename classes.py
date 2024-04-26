#   Classes is part of OOP

#   Key concepts:
#   class is a blueprint of attributes (vars/args) and methods (functions)
#   we can use class against an object
#   object is an instance of the class
#   allows us to easily make multiple objects of the same type.

# class Dog: # class names start with a capital letter.
#     energy = "high" # setting an attribute of the class

#     def speak(self): # Creating a method
#         print("bark")

# fido = Dog() # makes an object called fido of the dog class

# fido.speak() # call method through the object - only objects within the class can call a method in the class

# class Students:
#     pass

# student1 = Students()
# student2 = Students()

# student1.first = "john"
# student1.last = "smith"
# student1.age = 10

# print(student1.age, student1.first)

# class Student():
#     def __init__(self, first, last, age): # init method, called a dunder and is
#         self.first = first # init method inititises the object with these attributes
#         self.last = last # the self parameter refers to the object itself
#         self.age = age # self maps the class data to the object
    
#     student1 = Student("noveed", "muhammed", "38")
#     student2 = Student("amina", "hussain", "37")

# Student.student1

# parent child classes

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def eat(self):
        print(f"{self.name} is eating")

class Cat(Animal):
    def __init__(self,name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    my_cat = Cat("felix", "cat", "cat")

    my_cat.meow
    my_cat.eat()
