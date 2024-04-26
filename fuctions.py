## fuctions - a block of code - either performs a task or returns a value.
## repeatability

# def greet(name): # parameters that take in arguments
#     print(f"hi {name}")

# greet("Noveed")

## Passing Multiple Arguments

# def greet_1(first_name, second_name, age):
#     print(f"{first_name} {second_name} is {age}")

# greet_1("noveed", "muhammed", 38)

## better to use return as we can store the value
## stores in a variable or file
## print and input limit fuctionality

# def greeter(name):
#     return f"hello {name}"

# x = greeter("noveed")

# print(x)

## Default values

# def greet3(name, age=10): # default(S) needs to be at the end of the line
#     return f"{name} is {age}"

# print(greet3("noveed"))
# print(greet3("Noveed", 20))

## *args
## used if we dont know how many args will be passed through
## we add a * before parameter
## it will recieve a tuple of args.

# def fruite_list(*fruits):
#     print("the fruites are: ")
#     for fruit in fruits:
#         print(fruit)

# fruite_list("apple", "orange", "pear")

# def make_pizza(size, *toppings):
#     print(f"order for {size}-inch pizza, with the following toppings: ")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza(12, "chicken", "jalapeno", "onion")

## kwarg - keyword argument
## send args as key:value pairs.
## order therefore does not matter

# def fruit_list(fruit1, fruit2, fruit3):
#     print(f"Fav fruit is {fruit1}")
#     print(f"2nd fav fruit is {fruit2}")
#     print(f"3rd fav fruit is {fruit3}")

# fruit_list(fruit1="apple", fruit2="pear", fruit3="orange")

## **kwargs
## if we don't knopw how many kwargs there will be.

# def fav_food(**food):
#     print(f"fav food is", food["dessert"], "not", food["fruit"])

# fav_food(dessert="ice cream", fruit="apple", dairy="milk")

## / - a marker diving positional-only parameters from the rest
## before/ the params must be in order

# def example(a,b, /, c, d):
#     print(f"a - {a}, b - {b}, c = {c}, d = {d}")

# example(1, 2, d=4, c=3)

## passing a list as an arg

# def my_fuction(food):
#     for x in food:
#         print(x)

# list1 = ["apple", "pear", "orange"]

# my_fuction(list1)

##format

name = "Noveed"
age = 38
height = 1.8

print("my name is {}, i am {}, my height is {}".format(name, age, height))