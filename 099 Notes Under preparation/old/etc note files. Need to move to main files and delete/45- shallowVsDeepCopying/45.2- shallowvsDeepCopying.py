# https://realpython.com/copying-python-objects/

# Assignment statements in Python do not create copies of objects, they only bind names to an object.

# For immutable objects, that usually doesn’t make a difference as a copy is created.
# But for working with mutable objects or collections of mutable objects, or custome objects we need a way to create
# “real copies” or “clones” of these objects. Essentially, you’ll sometimes want copies that you can modify without
# automatically modifying the original at the same time.
#
# Here, we are going to look into how to copy or “clone” objects in Python 3 and some of the caveats involved.

# Let’s start by looking at how to copy Python’s built-in collections. Python’s built-in mutable collections like lists,
# dicts, and sets can be copied by calling their factory functions on an existing collection:
original_list = [1, 2, 3]
new_list = list(original_list)
# For lists, we can also use slicing
new_list2 = original_list[:]

original_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}
new_dict = dict(original_dict)

original_set = {1, 2, 3}
new_set = set(original_set)

# The difference between shallow and deep copying is only relevant for compound objects (objects that contain other
# objects, like lists or class instances) as the above methods won’t work for custom objects and, on top of that, it
# only creates shallow copies.
# For compound objects like lists, dicts, and sets, there’s an important difference between shallow and deep copying:

# A shallow copy means constructing a new collection/compound object and then populating it with the same references to
# the child objects as found in the original. In essence, a shallow copy is only one level deep. The copying process
# does not recurse and therefore won’t create copies of the child objects themselves.

# A deep copy makes the copying process recursive. It means first constructing a new collection/compound object and then
# recursively populating it with copies of the child objects found in the original. Copying an object this way walks the
# whole object tree to create a fully independent clone of the original object and all of its children.


