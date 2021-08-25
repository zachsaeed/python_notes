# Lists can contain any kind of element including other lists

nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8,  9]]

# used for complex dtata structures / matrices, game boards / mazes, rows
# and columns for visualisations, tabulation and grouping data

# to access
print(nested_lists[0][1])  # 2
print(nested_lists[1][-1])  # 6

# To access / print values in nested lists, we use nested for loops
for nested_list in nested_lists:
    for item in nested_list:
        print(item)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

