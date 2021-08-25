print('Using the copy module for shallow and deep copies of arbitrary objects:')
# Again the copy module comes to our rescue. Its copy.copy() and copy.deepcopy() functions can be used to duplicate any
# object.

# Once again, the best way to understand how to use these is with a simple experiment. I’m going to base this on the
# previous list-copying example. Let’s start by defining a simple 2D point class:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'
# I hope you agree that this was pretty straightforward. I added a __repr__() implementation so that we can easily
# inspect objects created from this class in the Python interpreter.

# Note: The above example uses a Python 3.6 f-string to construct the string returned by __repr__. On Python 2 and
# versions of Python 3 before 3.6 you’d use a different string formatting expression, for example:
def __repr__(self):
    return 'Point(%r, %r)' % (self.x, self.y)
# Next up, we’ll create a Point instance and then (shallowly) copy it, using the copy module:

a = Point(23, 42)
b = copy.copy(a)
# If we inspect the contents of the original Point object and its (shallow) clone, we see what we’d expect:
print(a)  # Point(23, 42)
print(b)  # Point(23, 42)
print(a is b)  # False

print(id(a))  # 4390776784
print(id(b))  # 4390887760

# Here’s something else to keep in mind. Because our point object uses immutable types (ints) for its coordinates,
# there’s no difference between a shallow and a deep copy in this case. But I’ll expand the example in a second.

# Let’s move on to a more complex example. I’m going to define another class to represent 2D rectangles. I’ll do it in a
# way that allows us to create a more complex object hierarchy (A coumpound object) —my rectangles will use Point
# objects to represent their coordinates:
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r}, '
                f'{self.bottomright!r})')

# Again, first we’re going to attempt to create a shallow copy of a rectangle instance:
rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
# If you inspect the original rectangle and its copy, you’ll see how nicely the __repr__() override is working out, and
# that the shallow copy process worked as expected:
print(rect)  # Rectangle(Point(0, 1), Point(5, 6))
print(srect)  # Rectangle(Point(0, 1), Point(5, 6))
rect is srect  # False
print(id(rect))  # 4367981200
print(id(srect))  # 4367981520

# Remember how the previous list example illustrated the difference between deep and shallow copies? I’m going to use
# the same approach here. I’ll modify an object deeper in the object hierarchy, and then you’ll see this change
# reflected in the (shallow) copy as well:
rect.topleft.x = 999
print(rect)  # Rectangle(Point(999, 1), Point(5, 6))
print(srect)  # Rectangle(Point(999, 1), Point(5, 6))
print('This is because they are the same objects:')
print(id(rect.topleft))  # 4373195152
print(id(srect.topleft))  # 4373195152

# I hope this behaved how you expected it to. Next, I’ll create a deep copy of the original rectangle. Then I’ll apply
# another modification and you’ll see which objects are affected:
import copy
drect = copy.deepcopy(srect)
drect.topleft.x = 222
print(drect)  # Rectangle(Point(222, 1), Point(5, 6))
print(rect)  # Rectangle(Point(999, 1), Point(5, 6))
print(srect)  # Rectangle(Point(999, 1), Point(5, 6))

# This time the deep copy (drect) is fully independent of the original (rect) and the shallow copy (srect).
# We’ve covered a lot of ground here, and there are still some finer points to copying objects.

# 3 Things to Remember
# - Making a shallow copy of an object won’t clone child objects. Therefore, the copy is not fully independent of the
#   original.
# - A deep copy of an object will recursively clone child objects. The clone is fully independent of the original, but
#   creating a deep copy is slower.
# - You can copy arbitrary objects (including custom classes) with the copy module.

