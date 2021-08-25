# REVISION
# Enumerate and zip are two of the most powerful tools when constructing a for-loop
#
# Enumerate
# A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the
# programmers’ task by providing a built-in function enumerate() for this task.

# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object. This enumerate object
# can then be used directly in for loops or be converted into a list of tuples using list() method.

# This way, there is no need to create and initialise a counter variable anymore in a for-loop using counter = 0
# (initialisation) and counter += 1 (inside loop).

# Syntax:
# class-enumerate-Tuples = enumerate(iterable, start=0)
# Where:
#   Iterable: any object that supports iteration
#   Start: the index value from which the counter is to be started, by default it is 0

l1 = ["eat","sleep","repeat"]
s1 = "geek"

# creating enumerate objects
obj1 = enumerate(l1)
obj2 = enumerate(s1)

print("Return type:",type(obj1))  # Return type: <class 'enumerate'>
print(list(enumerate(l1)))  # [(0, 'eat'), (1, 'sleep'), (2, 'repeat')]
# changing start index to 2 from 0
print(list(enumerate(s1, 2)))  # [(2, 'g'), (3, 'e'), (4, 'e'), (5, 'k')]

# Python program to illustrate numerate function in loops
l1 = ["eat","sleep","repeat"]
# printing the tuples in object directly
for ele in enumerate(l1):
    print(ele)
# (0, 'eat')
# (1, 'sleep')
# (2, 'repeat')

# changing index and printing separately
for count,ele in enumerate(l1,100):
    print(count,ele)
# 100 eat
# 101 sleep
# 102 repeat

# Example with zip and enumerate togather:
upperCase = ['A', 'B', 'C', 'D', 'E', 'F']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f']
for i, (upper, lower) in enumerate(zip(upperCase, lowerCase), 1):
    print(f'{i}: {upper} and {lower}.')
# 1: A and a.
# 2: B and b.
# 3: C and c.
# 4: D and d.
# 5: E and e.
# 6: F and f.

# Note: In the above code:
print(list(zip(upperCase, lowerCase)))  # [('A', 'a'), ('B', 'b'), ('C', 'c'), ('D', 'd'), ('E', 'e'), ('F', 'f')]
print(list(enumerate(zip(upperCase, lowerCase), 1)))  # [(1, ('A', 'a')), (2, ('B', 'b')), (3, ('C', 'c')), (4, ('D', 'd')), (5, ('E', 'e')), (6, ('F', 'f'))]
