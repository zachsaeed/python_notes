# range(start, stop[, step])
# where start is optional. Default = 0
# stop is mandatory
# step is optional. defaults to 1

# The range type represents an immutable sequence of numbers and is commonly used for looping a specific number of times
# in for loops.

# The advantage of the range type over a regular list or tuple is that a range object will always take the same (small)
# amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values,
# calculating individual items and subranges as needed).

var_range = range(10)
print(var_range)  # range(0, 10)
print(type(var_range))  # <class 'range'>

for item in var_range:
    print(item)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# We can type cast to list or tuple
print(list(var_range))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(tuple(var_range))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

print(list(range(0, 10, -2)))  # []
# for -ve step it counts backward. Therefore start should be greater than stop:
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]

# +ve step, start > stop
print(list(range(-10, 10, 2)))  # [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8]
# -ve step, start < stop
print(list(range(10, -10, -2)))  # [10, 8, 6, 4, 2, 0, -2, -4, -6, -8]
# otherwise it will print []


# Range methods
#
# There are only 2 range methods, index() and count() which are common methods within all sequence types therefore,
# discussed in a separate topic.
