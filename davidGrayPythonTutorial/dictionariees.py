# Dictionaires 
# what we'd refer to as objects in JS

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

# using constructors to create dict
band2 = dict(vocals = "Plant", guitar='Page')

print(band)
print(band2)
print(type(band2))
print(len(band2))


# Accessing items in a dict
print(band['vocals'])
print(band.get('guitar'))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key/value pairs as tuples
print(band.items())

# verify a key exxist in a dict
print('guitar' in band)
print('triangle' in band2) 

# change values 
band['vocals'] = 'Coverdale'
band.update({'bass': 'AySongz'})

print(band)


# remove items 
print(band.pop('bass'))
print(band)

band['drums'] = 'Iya Ilu'
print(band)

print(band.popitem())
print(band)

# delete and clear
band['drums'] = 'Iya Ilu'
del band['drums']
print(band)

band2.clear()
print(band2)

del band2

# copying dictionaries

# band2 = band # this method only creates a refeence not a new dict
# print('Bad way to copy!')
# print(band2)
# print(band)

# band2['drums'] = 'Ola'
# print(band) # proof the above method is just a copy so don't use!

band2 = band.copy()
band2['drums'] = 'Ola'
print('Good copy!')
print(band2) 
print(band) 


# copying dict using the dict() constructor function
band3 = dict(band)
print(band3)


# Nest Dictionaires 
member1 = {
    'name': 'Plant',
    'instrumentalist' : 'guitar'
}
member2 = {
    'name': 'Page',
    'instrumentalist' : 'guitar'
}

band = {
    'member1': member1,
    'meember2': member2
}
print(band)
print(band['member1']['name'])  # Plant



# Sets
nums = {1, 2, 3, 4}
nums2 = set((5,6,7,8))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))

# No dupicates allowed 
nums = {1,2,2,3}
print(nums)

# True is a duplicae of 1 and false is a duplicte of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)


# check if a value is in a set
print(2 in nums)


# but you cannot refer to an element in the set with an index psition or a key

# Adding a new value to a set
nums.add(8)
print(nums)

# add elements from one set to another
morenums = {5 ,6, 7}
nums.update(morenums)
print(nums)
# you can use update wth lists and tuples

# merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print(mynewset)


# keep only the dupicates
three = {1, 2, 3}
four = {2, 3, 4}

three.intersection_update(four)
print(three)


# keep all except the dupicates
five = {1, 2, 3}
six = {2, 3, 4}

five.symmetric_difference_update(six)
print(five)

# you can use . to pull up different formulas 