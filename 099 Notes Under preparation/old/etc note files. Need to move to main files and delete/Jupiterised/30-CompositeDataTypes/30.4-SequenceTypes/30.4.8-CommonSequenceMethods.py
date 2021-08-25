# index(), count() are available in string, list, tuple, bytearray and bytes sequences and discussed in a separate topic.

# --- strings:
s = "Syed Saquib Saeed"

# index( str_value [, startIndex, EndIndex] ):
# Finds the position of the first occurrence a given str_value in a list
# We can also provide a start index only or both startIndex (Inclusive) and endIndex (Exclusive) to search thru
print(s.index('S'))  # 0
print(s.index('aqui'))  # 6
print(s.index('Sa', 7, 100))  # 12
# print(s.index('Z'))  # ValueError: Z is not in the ist

# count( str_value ):
# print the number of times str_value appears in the list
print(s.count('Sa'))  # 2
print(s.count('Z'))  # 0

# --- lists and tuples (Same for tuples)
first_list = [1, 2, 3, 4, 4, 4, 4]

# index( item_value [, startIndex, EndIndex] ):
# Finds the position of the first occurrence a given item_value in a list
# We can also provide a start index only or both start and end indexes to search thru
print(first_list.index(2))  # 1
print(first_list.index(4))  # 3
first_list = [5, 5, 6, 7, 5, 8, 8, 9, 10]
print(first_list.index(5))  # 0
print(first_list.index(5, 1))  # 1
print(first_list.index(5, 2))  # 4
print(first_list.index(8, 6, 8))  # 6

# count( item_value ):
# prints the number of times item_value appears in the list
print(first_list.count(5))  # 3
print(first_list.count(22))  # 0


# --- range
var_range = range(0, 100, 2)

# index( item_value )
print(var_range.index(2))  # 1
print(var_range.index(4))  # 2
# Note: there's no requirement for index() to implement the 3 argument form
# print(var_range.index(4, 10, 19))   # TypeError: index() takes exactly one argument (3 given)

# count( item_value ):
# prints the number of times item_value appears in the list
print(var_range.count(5))  # 0
print(var_range.count(6))  # 1
# print(first_list.count(22))  # ValueError: 22 is not in the ist