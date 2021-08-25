# Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned.
# While tuples are immutable lists, frozensets are immutable sets.

# Sets being mutable are unhashable, so they can't be used as dictionary keys. On the other hand, frozensets are
# hashable and can be used as keys to a dictionary.

# Frozensets can be created using the function frozenset().
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# This datatype supports methods like copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(),
# symmetric_difference() and union().
# Being immutable it does not have method that add or remove elements.

print(A.isdisjoint(B))  # False
print(A.difference(B))  # frozenset({1, 2})
print(A | B)  # frozenset({1, 2, 3, 4, 5, 6})
# print(A.add(3))  # AttributeError: 'frozenset' object has no attribute 'add'
