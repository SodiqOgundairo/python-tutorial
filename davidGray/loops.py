# WHILE LOOP

# value = 1
# while value <= 10:
#     print(value) # this will run endlessly === infinite loop
#     if value == 5:
#         break
#     value += 1 # we can add this

# while value <= 10:
#     value += 1
#     if value == 5:  # this will be skipped
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))


# FOR LOOP
# names = ["Yemi", "Tolu", "Ayobami"]
# for x in names:
#     print(x)


# for x in "Misssissippi":
#     print(x)

# for x in names:
#     if x == "Tolu":
#         break
#     print(x)

# for x in names:
#     if x == "Tolu":
#         continue
#     print(x)


# range will start on the number you start on andwill skip the last number
# for x in range(4):
# print(x)


# for x in range(2, 4):
#     print(x)

# for x in range(
#     0, 100, 4
# ):  # increment form 0 to 100 with the dividend of 4 (or whatever the last digit is)
#     print(x)
# else:
#     print("Glad that's over!")


# nested loops

names = ["Yemi", "Tolu", "Ayobami"]
actions = ["codes", "eats", "sleeps"]

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

for action in actions:
    for name in names:
        print(name + " " + action + ".")

# find practical loops sin user_input.py
