# r = Read
# a = Append
# w = Write
# x = Create

import os

# Read - error if it doens't exist
f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open('names.txt')
    print(f.read())
except FileNotFoundError:
    print('The file does not exist')
finally:
    f.close()


# Append - creates the file if it does not exists
f = open('names.txt', 'a')
f.write('\nNeil')
f.close()

f = open('names.txt')
print(f.read())
f.close()


# Write (overwrites) - creates the file if it doesn't exists
f = open('context.txt', 'w')
f.write('I deleted all of the context')
f.close()

f = open('context.txt')
print(f.read())
f.close()


# Two ways to create a new file,

# using w if the file doesn't exists it creates it
f = open('newfile.txt', 'w')
f.close()


# using x if the file exists it throws an error if not it creaetes it

if not os.path.exists('Yemi.txt'):
    f = open('Yemi.txt', 'x')
    f.close()


# delete a file
# avoid an error if it doesn't exist
if os.path.exists('newfile.txt'):
    os.remove('newfile.txt')
else:
    print('The file does not exist')


# replace the content of a file with another
with open('more_names.txt') as f:
    content = f.read()

with open('names.txt', 'w') as f:
    f.write(content)
