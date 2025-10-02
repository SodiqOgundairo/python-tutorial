class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"


# person1 = Person('Yemi', 25, 270)
# print(person1.name)
# print(person1.age)
# print(person1.height)

# person2 = Person('Tolu', 30, 180)
# print(person2.name)
# print(person2.age)
# print(person2.height)

# person2.name = 'Racheal'
# print(person2.name)

# print(person2)

# print(Person.amount)


# INHERITANCE

class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

# to print the salary along with the other details, we need to append the __str__ method
    def __str__(self):
        text = super(Worker, self).__str__()
        # text += ", Salary {}". format(self.salary)
        text += f", Salary {self.salary}"
        return text

    def calc_yearly_salary(self):
        return self.salary * 12


worker1 = Worker('Ayobami', 40, 170, 2000)
print(worker1)
print(worker1.calc_yearly_salary())


# OPERATOR OVERLOADING
class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"


v1 = Vector(2, 5)
v2 = Vector(3, 7)

print(v1)
print(v2)

v3 = v1 + v2
print(v3)
