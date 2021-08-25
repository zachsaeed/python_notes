print('Making deep copies:')
# Had we created a deep copy of xs in the first step, both objects would’ve been fully independent. This is the
# practical difference between shallow and deep copies of objects.

# Now you know how to create shallow copies of some of the built-in collection classes, and you know the difference
# between shallow and deep copying. The questions we still want answers for are:
# How can you create deep copies of built-in collections?
# How can you create copies (shallow and deep) of arbitrary objects, including custom classes?
# The answer to these questions lies in the copy module in the Python standard library. This module provides a simple
# interface for creating shallow and deep copies of arbitrary Python objects.

# Let’s repeat the previous list-copying example, but with one important difference. This time we’re going to create a
# deep copy using the deepcopy() function defined in the copy module instead:
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
zs = copy.deepcopy(xs)

# When you inspect xs and its clone zs that we created with copy.deepcopy(), you’ll see that they both look identical
# again—just like in the previous example:
print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(zs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# However, if you make a modification to one of the child objects in the original object (xs), you’ll see that this
# modification won’t affect the deep copy (zs).

# Both objects, the original and the copy, are fully independent this time. xs was cloned recursively, including all of
# its child objects:
xs[1][0] = 'X'
print(xs)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
print(zs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# This is because the child objects are copies too:
print('Prove that child objects are copies too:')
print(id(xs[0]))  # 4302850720
print(id(zs[0]))  # 4302883488


print('Copying Arbitrary Python Objects')
# The question we still need to answer is how do we create copies (shallow and deep) of arbitrary objects, including
# custom classes. Let’s take a look at that now.

print('Copy by reference:')
# Let's quickly see what happens if you copy your custom class:
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

my_class = MyClass([1, 2], [3, 4])
my_new_class = my_class

print(id(my_class))  # 140397059541368
print(id(my_new_class))  # 140397059541368

my_class.x[0] = 0
print(my_new_class.x)  # [0, 2]
# You see that by simply copying the class with the = , we get two references to the same object, and therefore the id
# is the same. Moreover, if one of the mutable attributes of the class changes, it will also change in all the other
# objects

