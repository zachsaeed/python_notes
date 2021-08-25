# Sets are mutable. But since they are unordered, indexing have no meaning.
# We cannot access or change an element of set using indexing or slicing. Set does not support it.

my_set = {1,3}

# adding elements to a set add() and update():

# Adds an item to set. I value already exists set will stay same as it doesnt store duplicates
my_set.add(2)
print(my_set)  # {1, 2, 3}

# add multiple elements
# We can add multiple elements using the update() method. The update() method can take tuples, lists, strings or other
# sets as its argument. In all cases, duplicates are avoided.
my_set.update([2,3,4])
print(my_set)  # {1, 2, 3, 4}
# add list and set
my_set.update([4,5], {1,6,8})
print(my_set)  # {1, 2, 3, 4, 5, 6, 8}

# remove elements from a set using discard, remove and pop
# The only difference between the two is that, while using discard() if the item does not exist in the set, it remains
# unchanged. But remove() will raise an error in such condition.
# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
my_set.discard(4)
print(my_set)  # {1, 3, 5, 6}

# remove an element
my_set.remove(6)
print(my_set)  # {1, 3, 5}

# discard an element not present in my_set
my_set.discard(2)
print(my_set)  # {1, 3, 5}

# remove an element  not present in my_set
# my_set.remove(2)  # KeyError: 2


# Similarly, we can remove and return an item using the pop() method.
# Set being unordered, there is no way of determining which item will be popped. It is completely arbitrary.
my_set = set("HelloWorld")
print(my_set)  # {'d', 'H', 'e', 'l', 'o', 'W', 'r'}

# pop an element
# Output: random element
print(my_set.pop())  # d

# pop another element
# Output: random element
my_set.pop()
print(my_set)  # {'e', 'l', 'o', 'W', 'r'}


# We can also remove all items from a set using clear().
# clear()
# Removes all contents of the set

# copy()
# makes a copy/clone of the set
# <clone_of_s> is <s>  # False


# Covered in next topic
# union()	Returns the union of sets in a new set
# intersection()	Returns the intersection of two sets as a new set
# difference()	Returns the difference of two or more sets as a new set
# symmetric_difference()	Returns the symmetric difference of two sets as a new set

# difference_update()	Removes all elements of another set from this set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
