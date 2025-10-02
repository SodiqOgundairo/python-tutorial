## writing strings is this way!
person = "Yemi"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")


message = "\n%s has %s coins left." % (person, coins)
print(message)

formatting = "\n{} has {} coins left.".format(person, coins)
print(formatting)

formatting = "\n{1} has {0} coins left.".format(person, coins)
print(formatting)

formatting = "\n{person} has {coins} coins left.".format(person=person, coins=coins)
print(formatting)

player = {"person": "Yemi", "coins": 3}

formatting = "\n{person} has {coins} coins left.".format(**player)
print(formatting)


# this is f_srings!
some_string = f"\n{person} has {coins} coins left (f-string)."
print(some_string)

some_string = f"\n{person} has {2 * 5} coins left (f-string)."
print(some_string)

some_string = f"\n{person.upper()} has {2 * 5} coins left (f-string)."
print(some_string)

some_string = f"\n{player['person'].lower()} has {2 * 5} coins left (f-string)."
print(some_string)


# passing formating options
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f} \n")

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

for num in range(1, 11):
    print(f"{num} divided by {num} 4.52 {num/4.52:.2%}")
