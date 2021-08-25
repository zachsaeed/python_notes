# Indexing and Slicing works the same for all sequence datatypes (strings, lists, tuples, byte and bytearray).
# Here we will use a string as an example.

# Characters in a string can be accessed using the standard [ ] syntax. Python uses zero-based indexing
# ie index positions starting from 0 or [-1] from the end

#   0   1  2  3  4  5  6  7  8  9  has indexes:
#   0   1  2  3  4  5  6  7  8  9 or
#  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# If the index is out of bounds for the string, Python raises an error.The Python style is to halt if it can't tell
# what to do, rather than just make up a default value.

# The [ ] syntax and the len() function actually work on any sequence type -- strings, lists,
# etc.. Python tries to make its operations work consistently across different types.
# NOTE: don't use "len" as a variable name to avoid blocking out the len() function. The '+' operator can concatenate
# two strings. Notice in the code below that variables are not pre-declared -- just assign to them and go.

# String Indices
# String characters can be accessed via their

s = '0123456789'
print(s[0])  # 0
print(s[2])  # 2
print('0123456789'[3])  # 3
print(s[-1])  # 9
print(s[-2])  # 8
# print(s[10]) IndexError: string index out of range

# Note: for immutable sequence objects, we cannot change the values of the original object
# s[5] = 'a'   TypeError: 'str' object does not support item assignment

print('Slicing:')

# Python uses zero-based indexing ie index positions starting from 0 or [-1] from the end
s = '0123456789'
#  string:            0   1  2  3  4  5  6  7  8  9
#  has indexes:       0   1  2  3  4  5  6  7  8  9
#  has -ve indexes:  -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# The "slice" syntax is a handy way to refer to/extract sub-parts of sequences.
# The slice 's[startIndex(inclusive):endIndex(Exclusive):stepCount]' returns the elements beginning at start and
# extending up to but not including end. Step will define the size of each step moving from startIndex to endIndex.

print(s[1:4])  # '123' -- chars starting at index 1 and extending up to but not including index 4
print(s[:])  # '0123456789' -- omitting either index, defaults to the start or end of the string

# -ve values for start and end
# Negative index numbers count back from the end of the string:
print(s[:-3])  # '0123456' -- starts from 0 to position to -3 (excluding position -3)
print(s[-3:])  # '789' -- starting from -3 position and extending to the end of the string (len(s)).

# Step Parameter:
# step parameter defines the number to count at a time. It defaults to 1 when not used.
print(s[0:10:1])  # 0123456789
print(s[::2])  # 02468
print(s[1::2])  # 13579
# 'startIndex' should be to the left of 'endIndex' if the 'step' is +ve otherwise it will return an empty string. In
# other words, elements are fetched starting from left to right for a positive 'step'.
# The opposite is true for a -ve Index

# NOTE: The end index is not a count but an index position. This is proved by the fact that when we use +ve step, the
# endIndex should be to the right of the start index and vice versa.

# INTERVIEW
# Note: using Negative step.
# 'startIndex' should be to the right of 'endIndex' if the 'step' is -ve otherwise it will return an empty string. In
# other words, elements are fetched starting from right to left for a negative 'step'.
print(s[:1:-1])  # 98765432
print(s[5:1:-1])  # 5432

print(s[::-1])  # 9876543210  # NOTE: reverses the string
# Same as
print(s[-1:-11:-1])  # 9876543210


# INTERVIEW
# Note: Some side cases:
print(s[:])  # '0123456789' -- omitting both always gives us a copy of the whole thing (this is the pythonic way to copy
# a sequence like a string or list where default values are start=0, end =len(s) & step=1)

print(s[1:100])  # '123456789' -- an index that is too big is truncated down to the string length.
#   It does not throw an error like single index does

# It is a neat truism of slices that for any index n, s[:n] + s[n:] == s. This works even for n negative or out of
# bounds. Or put another way s[:n] and s[n:] always partition the string into two string parts, conserving all the
# characters.
print(s[:1])  # 0
print(s[1:])  # 123456789
print(s[:1]+s[1:])  # 0123456789

print(s[::])  # 0123456789
# same as:
print(s[0:len(s):1])  # 0123456789

print(s[::-1])  # 9876543210  #reverses the list
print(s[-1:-11:-1])  # 9876543210
