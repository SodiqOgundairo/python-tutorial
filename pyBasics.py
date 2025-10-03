# data types
from enum import Enum
name = "Yemi"  # str
age = 19  # int
is_student = True  # bool
height = 5.9  # float
fruits = ["apple", "banana", "cherry"]  # list / array / tuples
person = {"name": "Yemi", "age": 19}  # dict / object
# complex data types
coordinates = (10.0, 20.0)  # tuple


_jes = '20'
# print(_jes) # 20
# print(type(_jes)) # <class 'str'>

# print(str(age) + " is the age of " + name)


# Boolean Operations
condition1 = True
condition2 = False

# print(condition1 and condition2) # False
# print(condition1 or condition2)  # True
# print(not condition1)            # False


# Tenary Operator

def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# print(is_adult(20))  # True
# print(is_adult(17))  # False


# Strings
text = 'Technovates'
# print(text[0])  # T
# print(text[-1])  # s
# print(text.lower())  # technovates
# print(text.upper())  # TECHNOVATES
# print(text.replace('Tech', 'Code'))  # Codenovates
# print(text.split('n'))  # ['Tech', 'ovates']
# print('Tech' in text)  # True
# print(len(text))  # 11
escape_str = "He said, \"Hello!\""
# print(escape_str)  # He said, "Hello!"

# Python doesn't have a way to enforce a constant variable instead you can use naming conventions
# to indicate that a variable should not be changed (WRITING CONSTANTS IN CAPITAL LETTERS). ALSO, enum module can be used to create constant variables.


class Constants(Enum):
    PI = 3.14
    E = 2.71
    GRAVITY = 9.81
# print(Constants.PI.value)  # 3.14
# print(Constants.E.value)   # 2.71
# print(Constants.GRAVITY.value)  # 9.81


# ENUMS
# Enums are a way to define a set of named constant values. They are useful for representing a fixed set of related values, such as days of the week, months of the year, or states in a state machine.


# USER INPUT this works for cli applications other kinds of applications have different ways of getting user input
# user_name = input("Enter your name: ")
# print("Hello, " + user_name + "!")

# CONTROL STATEMENTS
def check_number(num):
    if num > 0:
        return "Positive"
        # print("This is a positive number")
    elif num < 0:
        return "Negative"
        # print("This is a negative number")
    else:
        return "Zero"
        # print(check_number(10))  # Positive


# test_control = input("Enter True or False: ")
# test_control = True
# if test_control == "True":
#     print("This is True")
# elif test_control == "False":
#     print("This is False")
# else:
#     print("Invalid input")

# greeting = input("Enter a greeting (morning, afternoon, evening): ").lower()
# greeting = 'morning'
# if greeting == 'morning':
#     print("Good morning!")
# elif greeting == 'afternoon':
#     print("Good afternoon!")
# elif greeting == 'evening':
#     print("Good evening!")
# else:
#     print("Hello!")


a = 2
result = 2 if a == 0 else 3 if a == 1 else 4
# print(result)  # 4


# LISTS
dogs = ["Bulldog", "Beagle", "Poodle", 1, 2.5, True]
# print(dogs[0])  # Bulldog
# print(dogs[-1])  # True
# print(dogs[1:4])  # ['Beagle', 'Poodle', 1]
# print(dogs.index("Beagle"))  # 1
# append_result = dogs.append("Labrador")  # Adds "Labrador" to the end of the list
# print(dogs)  # ['Bulldog', 'Beagle', 'Poodle', 1, 2.5, True, 'Labrador']
# remove_result = dogs.remove("Poodle")  # Removes "Poodle" from the list
# print(dogs)  # ['Bulldog', 'Beagle', 1, 2.5, True, 'Labrador']
# pop_result = dogs.pop()  # Removes and returns the last item in the list
# print(pop_result)  # Labrador
# print(dogs)  # ['Bulldog', 'Beagle', 1, 2.5, True]
# dogs.sort(key=str)  # Sorts the list in ascending order (converts all elements to strings for comparison)
# print(dogs)  # [1, 2.5, 'Beagle', 'Bulldog', True]
# dogs.reverse()  # Reverses the order of the list
# print(dogs)  # [True, 'Bulldog', 'Beagle', 2.5, 1]

# dogscopy = dogs.copy()  # Creates a shallow copy of the list
# print(dogscopy)  # [True, 'Bulldog', 'Beagle', 2.5, 1]
# dogs.clear()  # Removes all items from the list


# TUPLES
# you can't change tuples they are immutable unlike LISTS
objects = ("Table", "Chair", "Lamp", 1, 2.5, False)
# print(objects[0:3])  # ('Table', 'Chair', 'Lamp')
# print(objects[1:])  # ('Chair', 'Lamp', 1, 2.5, False)


# DICTIONARIES
# collections of keys and values pairs
person = {"name": "Yemi", "age": 19, "is_student": True,
          "height": 5.9, "fruits": ["apple", "banana", "cherry"]}
# print(person["name"])  # Yemi
# print(list(person.keys()))  # ['name', 'age', 'is_student', 'height', 'fruits']
# print(list(person.values()))  # ['Yemi', 19, True, 5.9, ['apple', 'banana', 'cherry']]


# SETS
# sets are unordered collections of unique elements, just like dictionaries but without key-value pairs.
unique_numbers = {1, 2, 3, 4, 5, 1, 2}
unique_str = {"apple", "banana", "cherry", "apple"}
# print(unique_numbers)  # {1, 2, 3, 4, 5}
# unique_numbers.add(6)  # Adds 6 to the set
# print(unique_numbers)  # {1, 2, 3, 4, 5, 6}
# unique_numbers.remove(3)  # Removes 3 from the set (if it exists)
# print(unique_numbers)  # {1, 2, 4, 5, 6}
# unique_numbers.discard(10)  # Removes 10 from the set if it exists, does nothing if it doesn't
# print(unique_numbers)  # {1, 2, 4, 5, 6}
# print(len(unique_numbers))  # 5
# # unique_numbers.clear()  # Removes all elements from the set
# # print(unique_numbers)  # set()

# print(unique_str | unique_numbers)  # Union
# print(unique_str & unique_numbers)  # Intersection
# print(unique_str - unique_numbers)  # Difference
# print(unique_str ^ unique_numbers)  # Symmetric Difference
# print("banana" in unique_str)  # Membership Test
# print("orange" in unique_str)  # Membership Test
# print(len(unique_str))  # Length
# print(sorted(unique_str))  # Sorted List of Elements


# FUNCTIONS
name = 'Yemi'


def greet(name):
    return "Hello, " + name + "!"

# print(greet(name))  # Hello, Yemi!
# print(greet("John"))  # Hello, John!
# print(greet(name="Alice"))  # Hello, Alice!


# OBJECTS
# EVERYTHING IN PYTHON IS AN OBJECT
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"


# LOOPS {we have 2 kind of loops}
# While Loops
loop_test = True
while loop_test == True:
    # print('while loop working')
    loop_test = False
    # print('Loop ends here')


# For Loops
items_s = [1, 2, 3, 4]
# for item in items_s:
#     print('for loop working')

# for item in range(len(items_s)):
#     print('item:', items_s[item])
# print('for loop ends here')

# for item in range(4):
#     print('item:', item)
# print('for loop ends here')

# for index, item in enumerate(items_s):
#     print('index:', index, 'item:', item)


# break and continue statements are used to interrupt loops in a block
# continue stops the current iteration and moves to the next iteration
# break stops the entire loop

for item in items_s:
    if item == 2:
        continue  # Skip the rest of the loop when item is 2
    if item == 3:
        break  # Exit the loop when item is 3
    # print('item:', item)


# CLASSES
# Classes are blueprints for creating objects. They encapsulate data for the object and methods to manipulate that data.

# class CatClass:
    # class content

# __init__ is a special method called a constructor that is automatically called when an object of the class is created.
# It is used to initialize the attributes of the class.
class Cat1:
    def __init__(self, name, color):
        self.name = name
        self.color = color

# creating an object
    def meow(self):
        return "Meow!"


# Creating an object of the Cat class
my_cat = Cat1("Whiskers", "Gray")
# print(my_cat.name)  # Whiskers
# print(my_cat.color)  # Gray

# print(my_cat.meow())  # Meow!


# we can create another animal with the method walk()
class Animal:
    def walk(self):
        print('walking')

# then create a cat class that inherits from Animal class


class Cat(Animal):
    def my_cat(self):
        print('meow')

# creating a new object of class Cat will have the walk() method from Animal class
# my_cat = Cat()
# my_cat.walk()  # walking
# my_cat.my_cat()  # meow


# MODULES
# Every python file is a module that can be imported to another python file
# two ways to import modules

# # 1 import all contents of a module
# import main
# main.Hello()  # Hello, World! Yemi is here!


# # 2 import specific function or class from a module
# from main import Hey
# Hey()  # Hey, I\'m imported form another file


# # if you have a module in a subdirectory you should create an empty __init__.py file in that directory
# from lib import greeting
# greeting.Hello()  # this is the file in the lib folder


# from lib.greeting import hola
# hola()  # this is the specific class called in the lib folder


# some modules in python are
# math
# import math
# math.sqrt(16)  # 4.0
# or

# from math import pi, sqrt
# print(pi)  # 3.141592653589793
# print(sqrt(25))  # 5.0

# re
# json
# datetime
# sqlite3
# os
# random
# statistics
# requests
# http
# urlib
#  and many more


# PEP8 is a style guide for python code that helps to write clean and readable code
# you can use pylint or flake8 to check your code for PEP8 compliance
# indent using 4 spaces
# max line length of 79 characters
# use blank lines to separate functions and classes
# use docstrings to describe functions and classes
# write each statement on its own line
# use spaces around operators and after commas
# python files are encoded in UTF-8 by default
# etc.


# DEBUGGING
# you can use print statements to debug your code
# you can use assert statements to check for conditions that should be true
# you can use logging module to log messages to a file or console
# you can use pdb module to set breakpoint() and step through your code


# VARIABLE SCOPES
# same local and global scopes works the same as other programming languages


# LAMBDA FUNCTIONS
# lambda functions are small anonymous functions that can take any number of arguments but can only have one expression
# they are often used as arguments to higher-order functions like map(), filter(), and reduce()
# works like arrow functions in javascript
def lambda_add(x, y): return x + y
# print(lambda_add(2, 3))  # 5


# RECURSION
# recursion is a programming technique where a function calls itself to solve a problem
# it is often used to solve problems that can be broken down into smaller subproblems
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# print(factorial(5))  # 120
# print(factorial(0))  # 1
# print(factorial(3))  # 6


# NESTED FUNCTIONS
# nested functions are functions defined inside other functions
def outer_function2(phrase):
    def inner_function(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        inner_function(word)

# outer_function2("Hello from Yemi")


# example 2
def count():
    counter = 0

    def increment():
        nonlocal counter  # Allows access to the counter variable from the outer function
        counter += 1
        print(counter)
    increment()
# count()  # 1


# CLOSURES
# closures are functions that remember the values from their enclosing lexical scope even when the program flow is no longer in that scope
def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


closure = outer_function("Hello, World!")
# closure()  # Hello, World!


# example 2
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

# print(double(5))  # 10
# print(triple(5))  # 15


# DECORATORS
# decorators are functions that modify the behavior of other functions or methods
# just like higher-order or callback functions in javascript
def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed this before {}".format(
            original_function.__name__))
        return original_function()
    return wrapper_function

# @decorator_function
# def display():
    # print("Display function executed")
# display() # 'Display function executed'


# each time display() is called it will run the wrapper_function() instead of the original display() function before running the original display() function
# output:
# Wrapper executed this before display
# Display function executed


# DOCSTRING
# docstrings are special strings that are used to document functions, classes, and modules they are used like comments but they can be accessed programmatically using the __doc__ attribute
# they are written using triple quotes (""" """)

def example_function():
    """This is an example function that does nothing."""
    pass


# INTROSPECTION
# introspection is the ability of a program to examine the type or properties of an object at runtime
# you can use the type() function to get the type of an object

def example(n):
    return n + 1
# print(type(example))  # <class 'function'>
# print(type(5))  # <class 'int'>

# you can use the dir() function to get a list of attributes and methods of an object
# print(dir(example))  # ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

# print(dir(5))  # ['__abs__', '__add__', '__and__', '__annotations__', '__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__float__', '__floor__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rsub__', '__rtruediv__', '__str__', '__sub__', '__subclasshook__', '__truediv__']


# you can use the hasattr() function to check if an object has a specific attribute or method
# print(hasattr(example, '__call__'))  # True
# print(hasattr(5, '__call__'))  # False


# ANNOTATIONS
# annotations are a way to add metadata to functions, classes, and variables
# they are used to provide hints about the types of arguments and return values of functions
def add(x: int, y: int) -> int:
    return x + y


# print(add(2, 3))  # 5
# varables can also be annotated
annotated_var: int = 0


# EXCEPTIONS
# exceptions are errors that occur during the execution of a program
# they can be handled using try-except blocks

# try:
#     result = 10 / 0 ## change this figure to see difference
#     print(result)
# except ZeroDivisionError as e:
#     print("Error occurred:", e)
# except Exception as e:
#     print("Some other error occurred:", e)
# else:
#     print("No errors occurred. Result is:", result)
# finally:
#     print("This block always executes.")


# result = 2 / 0
# print(result)  # This will raise a ZeroDivisionError


# try:
#     result = 2 / 0
# except ZeroDivisionError:
#     print("Error occurred: Division by zero is not allowed.")
# finally:
#     result = 2 / 2  # Ensure result is defined

# print("Result is:", result)  # Result is: 1


# RAISE EXCEPTIONS
# try:
#     raise Exception("This is a custom exception")
# except Exception as e:
#     print("Caught an exception:", e)

# # you can also define your own exception classes by inheriting from the built-in Exception class
# class CustomError(Exception):
#     pass # pass means do nothing

# try:
#     raise CustomError("This is a custom error")
# except CustomError as e:
#     print("Caught a custom error:", e)


# THE WITH STATEMENT
# the with statement is used to wrap the execution of a block with methods defined by a context manager
# it is often used to manage resources like file streams

filename = 'lib/greeting.py'
# instead of writing:

# try:
#     f = open(filename, "r")
#     content = f.read()
#     print(content)
# finally:
#     f.close()

# # you can write:
# with open(filename, "r") as f:
#     content = f.read()
#     print(content)


# # LIST COMPREHENSIONS
# list comprehensions are a concise way to create lists
numbers_list = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers_list]
# print(squared)  # [1, 4, 9, 16, 25]

even_numbers = [x for x in numbers_list if x % 2 == 0]
# print(even_numbers)  # [2, 4]


# equivalent to but better than the conventional for-loop below because it's more concise
numbers_list_2 = []
for x in numbers_list:
    numbers_list_2.append(x**2)
# print(numbers_list_2, 'This is conveentional for-loop')  # [1, 4, 9, 16, 25]

# even map and filter functions can be used but list comprehensions are more pythonic
squared_map = list(map(lambda x: x**2, numbers_list))
# print(squared_map, 'This is a map')  # [1, 4, 9, 16, 25]

squared_filter = list(filter(lambda x: x % 2 == 0, numbers_list))
# print(squared_filter, 'This is a filter')  # [2, 4]  # [1, 4, 9, 16, 25]

# DICTIONARY COMPREHENSIONS
squared_dict = {x: x**2 for x in numbers_list}
# print(squared_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

even_dict = {x: x**2 for x in numbers_list if x % 2 == 0}
# print(even_dict)  # {2: 4, 4: 16}


# POLYMORPHISM
# polymorphism is the ability of different classes to be treated as instances of the same class through a common interface
# it is often used to implement inheritance and interfaces in object-oriented programming
class Bird:
    def speak(self):
        return "Chirp!"


class Pig:
    def speak(self):
        return "Oink!"


animal1 = Bird()
animal2 = Pig()

print(animal1.speak())  # Chirp!
print(animal2.speak())  # Oink!


# OPERATOR OVERLOADING
# operator overloading is the ability to define custom behavior for operators like +, -, *, etc.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
print(v3)  # Vector(6, 8)


# VIRTUAL ENVIRONMENTS
# virtual environments are isolated python environments that allow you to manage dependencies for different projects
# you can create a virtual environment using the venv module
# python -m venv myenv
# source myenv/bin/activate  # on macOS/Linux
# myenv\Scripts\activate  # on Windows
# deactivate  # to exit the virtual environment
# you can use pip to install packages in the virtual environment
# pip install package_name
