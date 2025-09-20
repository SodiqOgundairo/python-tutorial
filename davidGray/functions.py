def hello_world():
    print("Hello world!")


hello_world()


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        # enforcing types
        return 0
    else:
        return num1 + num2


total = sum(7, 5)
print(total)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Dave", "John", "Sara")


def mult_named_items(**kwargs):  # kwargs = keyword arguments
    print(kwargs)
    print(type(kwargs))


mult_named_items(first="Dave", second="John", last="Sara")
