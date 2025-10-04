# a function that calls itself
# it might cause issues if not handled properly
# base case is important to avoid infinite recursion

num = 5

fact = 1

while num > 0:
    fact = fact * num
    num -= 1

print(fact)


def factorial(num):
    if num < 1:
        return 1
    else:
        number = num * factorial(num - 1)
        return number


print(factorial(5))


# EXAMPLE: FIBONACCI SEQUENCE

def fibonacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a


print(fibonacci(100))


# EXAMPLE: FIBONACCI SEQUENCE USING RECURSION
def fibonnaci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonnaci_recursive(n-1) + fibonnaci_recursive(n-2)


print(fibonnaci_recursive(100))


# recursion is not always smarter than iteration
# it can be less efficient and use more memory
# it can also lead to stack overflow if the recursion depth is too high
