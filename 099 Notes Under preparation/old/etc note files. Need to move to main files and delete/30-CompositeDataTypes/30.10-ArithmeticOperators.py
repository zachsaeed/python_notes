# Dictionaries compare equal if and only if they have the same (key, value) pairs (regardless of ordering). Order
# comparisons (‘<’, ‘<=’, ‘>=’, ‘>’) raise TypeError.

# --- Strings:

# String concatenation is done using the + operator
surname = "Saeed"
print("Syed" + " " + "Saquib" + " " + surname)
# we can also use the += operator
name = "Syed Saquib"
name += " Saeed"  # Same as, name = name + " Saeed"
print(name)

# Unlike Java, the '+' does not automatically convert numbers or other types to string form. The str() function
# converts values to a string form so they can be combined with other strings.
# pi = 3.14
# text = 'The value of pi is ' + pi  # TypeError: can only concatenate str (not "float") to str
# text = 'The value of pi is ' + str(pi)  # yes
# print(text)  # The value of pi is 3.14

# String multiplication is done using the * operator
# Concatenates the string with itself multiple times
print(surname * 2)  # SaeedSaeed

# --- List and tuples:
# Like string, range and tuples support + for merging two lists/tuples and
# * for inserting the same items multiple times

A = [1, 2, 3, 4, 5]
B = [5, 7, 8, 9, 0]
print(A + B)  # [1, 2, 3, 4, 5, 5, 7, 8, 9, 0]
print(A * 2)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# --- Range:
# Range does not support any of the arithmetic operators. However, the range can be typecasted to a list or tuple and
# the operators can be used then
# print(list(range(1,10)+range(11,15)))

# --- Sets
my_set = {1, 2, 3}
my_set2 = {3, 4, 5}
#print(my_set + my_set2)
#print(my_set * 2)
p#rint(my_set * my_set2)

# --- Dictionaries

