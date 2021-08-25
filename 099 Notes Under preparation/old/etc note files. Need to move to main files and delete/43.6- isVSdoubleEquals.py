# https://medium.com/peloton-engineering/the-dangers-of-using-is-in-python-f42941124027
# TODO https://www.pythonforthelab.com/blog/mutable-and-immutable-objects/

# The == operator compares the values of both the operands and checks for value equality.
# Whereas the 'is' keyword compares by reference. A reference is like a post-it note, an address, or a pointer to an
# object.
# In other words, it checks comparing both objects' id() values

list1 = []
list2 = []
list3 = list1

if (list1 == list2):
    print("True")
else:
    print("False")
# True   “True” because both list1 and list2 are empty lists.

if (list1 is list2):
    print("True")
else:
    print("False")
# False   "False" because two empty lists are at different memory locations. Hence list1 and list2 refer to different
# objects. We can check it with id() function in python which returns the “identity” of an object.
print(id(list1))  # 139877155242696
print(id(list2))  # 139877155253640


if (list1 is list3):
    print("True")
else:
    print("False")
# True