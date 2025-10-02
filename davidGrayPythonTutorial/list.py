users = ['Yemi', 'Racheal', 'Tolulope', 'Aaron']
data = ['Yemi', 19, True, 'black']

emptylist = []

print('Dave' in emptylist)

print(users[0])
print(users[-2])

print(users.index('Tolulope'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])


print(len(data))

users.append('Ogundairo')
print(users)

users+= ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
(print(users))

users.insert(0, 'Bob')
print(users)


# slice == replacing the values in the range indicated
users[2:2] = ['Eddie', 'Alex']
print(users)


users[1:3] = ['Robert', 'Ayobami', 'Titi', 'Bisi']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

data.clear()
print(data)

del data
# print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)


numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy.sort(reverse=True))

print(type(nums))

# creating list wth 'list' constructor
mylist = list((1, 'figo', True))
print(mylist)




# TUPLES
# much like list but it's data does not change you use () instead of []
mytuple = tuple(('Dave', 34, True))
tuple_without_constructor = (1, 2, 3, 4, 2, 2)

print(mytuple)
print(tuple_without_constructor)

print(type(mytuple))
print(type(tuple_without_constructor))

# you can only copy a tuple not change it's values 
newlist = list(mytuple)
newlist.append('Tolu')
newtuple = tuple(newlist)
print(newtuple)
print(type(newtuple))

# unpacking a tuple 
(one, *two, all) = tuple_without_constructor
print(one)
print(two)
print(all)

print(tuple_without_constructor.count(2))