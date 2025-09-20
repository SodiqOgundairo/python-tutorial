# Scopes
# Global scopes are variables accessible throughout the document WHILE
# local scope are variables defined inside a function which can't be accesed outide of the function
# works just like in general programming

name = "Yemi"  # global scope
count = 1


def greeting(name):
    color = "blue"
    print


def globalvar():
    # to modify global var you need to use the keyword global
    global count
    count += 1
    # if not it'd assume you create another local variable
    print(count)


globalvar()


# nonlocal keyword helps to access a local variable in a function from inside an indented function


def another():
    white = "True"

    def nested_def():
        nonlocal white
        print(white)

    nested_def()


another()


# RPS UPDATED
