# https://www.programiz.com/python-programming/set
# Sets can be used to carry out mathematical set operations like:
# union, intersection, difference and symmetric difference.
# We can do these operations with operators or methods.

#Let us consider the following two sets for the following operations.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# UNION (|)
# Union of A and B is a set of all elements from both sets without any duplicates
# Union is performed using | operator. Same can be accomplished using the method union().
print(A | B)  # {1, 2, 3, 4, 5, 6, 7, 8}

# We can also use union()
print(A.union(B))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(B.union(A))  # {1, 2, 3, 4, 5, 6, 7, 8}


# INTERSECTION (&)
# Intersection of A and B is a set of elements that are common in both sets.
# Intersection is performed using & operator. Same can be accomplished using the method intersection().
print(A & B)  # {4, 5}

# We can also use intersection()
print(A.intersection(B))  # {4, 5}
print(B.intersection(A))  # {4, 5}


# DIFFERENCE (-)
# Difference of A and B (A - B) is a set of elements that are only in A but not in B. Similarly, B - A is a set of
# element in B but not in A.
# Difference is performed using - operator. Same can be accomplished using the method difference().
print(A - B)  # {1, 2, 3}
print(B - A)  # {8, 6, 7}

# We can also use difference()
print(A.difference(B))  # {1, 2, 3}
print(B.difference(A))  # {8, 6, 7}


# SYMMETRIC DIFFERENCE (^)
# Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.
# (Basically, they are elements that are left in both sets after union)
# Symmetric difference is performed using ^ operator. Same can be accomplished using the method symmetric_difference().
print(A ^ B)  # {1, 2, 3, 6, 7, 8}
print(B ^ A)  # {1, 2, 3, 6, 7, 8}

# We can also use symmetric_difference()
print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}
print(B.symmetric_difference(A))  # {1, 2, 3, 6, 7, 8}


# Other set Operations:
# difference_update()	Removes all elements of another set from this set
# intersection_update()	Updates the set with the intersection of itself and another
# isdisjoint()	Returns True if two sets have a null intersection
# issubset()	Returns True if another set contains this set
# issuperset()	Returns True if this set contains another set
# symmetric_difference_update()	Updates a set with the symmetric difference of itself and another
