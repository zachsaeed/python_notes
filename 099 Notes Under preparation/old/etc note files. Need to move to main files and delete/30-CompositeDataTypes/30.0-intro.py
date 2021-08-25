# Composite Datatypes:
# All

# Sequence Types:
# - A sequence is a group of items with a deterministic ordering. The order in which we put them in is the order in
#   which we get an item out from them.
# - All python sequences have 'indexes' and can be 'sliced'.
# - Python offers 7 types of sequences:

# Text Sequence Type:
# 1 -  string (immutable, iterable)
# Sequence Types:
# 2 - list (mutable, iterable)
# 3 - tuples (immutable, iterable)
# 4 - range (immutable, iterable)
# Binary Sequence types: TODO: iterable?
# 5 - bytearray (mutable)
# 6 - byte (immutable)
# 7 - memoryview


# Collection (Mapping and Set Types):
# A collection, unlike a sequence, does not have a deterministic ordering. In a collection, while ordering is arbitrary,
# physically, they do have an order.  Python offers 3 types of collections:

# Mapping Type:
# 1 - dictionaries (mutable, iterable)
# Set Types
# 2 - sets (mutable, iterable)
# 2 - frozenset (immutable, iterable)

# mutable, immutable:
# Mutable can be changed after they are defined where as immutable cannot be changed. Instead, if we try to change
# something in an immutable object using the built-in methods, we get a new object and the original object stays the
# same.

# iterable
# - An iterator is an object that can be iterated upon, meaning that you can traverse through all the values by using it
#   with a ‘for in' loop
# - An iterator is an object that contains a countable number of values.
# - Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the
#   methods __iter__() and __next__().
# - (More on iterators and iterables in a separate section)
