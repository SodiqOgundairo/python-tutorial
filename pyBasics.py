## data types
name = "Yemi" ## str
age = 19 ## int
is_student = True ## bool
height = 5.9 ## float
fruits = ["apple", "banana", "cherry"] ## list / array / tuples
person = {"name": "Yemi", "age": 19} ## dict / object
## complex data types
coordinates = (10.0, 20.0) ## tuple


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
from enum import Enum

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
person = {"name": "Yemi", "age": 19, "is_student": True, "height": 5.9, "fruits": ["apple", "banana", "cherry"]}
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

print(greet(name))  # Hello, Yemi!
print(greet("John"))  # Hello, John!
print(greet(name="Alice"))  # Hello, Alice!


# OBJECTS
# EVERYTHING IN PYTHON IS AN OBJECT
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return "Woof!"
