# https://www.pythonforthelab.com/blog/deep-and-shallow-copies-of-objects/
print('__copy__ and __deepcopy__ methods:')
# It pays to go deep (ha!) on this topic, so you may want to study up on the copy module documentation. For example,
# objects can control how they’re copied by defining the special methods __copy__() and __deepcopy__() on them.

# With Python, you have a very high level of granularity regarding how much control you have on every step, including
# deep and shallow copies. In order to have control, you need to override the methods __copy__ and __deepcopy__, let's
# see how and then we see why. First, imagine that you want to be able to copy a class with all its references but one,
# which you need to be independent of one instance of your class to another. You can do:

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.other = [1, 2, 3]

    def __copy__(self):
        new_instance = MyClass(self.x, self.y)
        new_instance.__dict__.update(self.__dict__)
        new_instance.other = copy.deepcopy(self.other)
        return new_instance

# Let's go step by step. When you use copy.copy, the method that will be executed is __copy__ and the argument is the o
# bject itself. The return is going to be the copied object. To make a copy, the first thing is to instantiate the new
# class, which we do by calling MyClass again. You can make more general by replacing MyClass with type(self).

# Anyhow, the next step is to copy all the attributes of the base instance into the new one. This can be quickly done by
# updating the __dict__ attribute. If you are not familiar with it, we are going to quickly explore it later. These two
# steps alone define the standard behavior for a shallow copy of an object. In order to achieve a special functionality,
# we add one more line, in which the other attribute is copied with a deep copy. other was not part of the __init__ just
# to show you that we can add on any attribute of the class.

# Finally, if we repeat the simple tests of before, we would get:
import copy
my_class = MyClass([1, 2], [3, 4])
my_new_class = copy.copy(my_class)

print(id(my_class))  # 139816535263552
print(id(my_new_class))  # 139816535263720

my_class.x[0] = 0
my_class.y[0] = 0
my_class.other[0] = 0
print(my_new_class.x)  # [0, 2]
print(my_new_class.y)  # [0, 4]
print(my_new_class.other)  # [1, 2, 3]

# As you can see, the attribute other was deep copied and therefore if you change it in one class, it won't change in
# the other.

# About the dict attribute
# As you know, objects contain attributes, and these attributes are always defined as variables which in the end look
# like strings (i.e., you can read them, type them with your keyboard, etc.)

# This makes it possible to think the collection of attributes as a dictionary. In the class from the previous section,
# you can explore this idea by doing to following:
print(my_class.__dict__)  # {'x': [0, 2], 'y': [0, 4], 'other': [1, 2, 3]}
# I hope you are seeing the gist of this. You can also alter the __dict__ directly:
my_class.__dict__['x'] = [1, 1]
print(my_class.x)  # [1, 1]
# It means that you can either use the .x or the __dict__['x'] to work with the same element in your object. This is
# also a quick way of knowing all the attributes that are defined in your object, etc. Hope this short story can help
# clarify a topic that is not that trivial for newcomers to the deeps of object-oriented python programming.

# Custom deep copy
# Back in the track to the main topic of the article, we need to customize the deep copy of the class. It is very
# similar to the __copy__ method, but it takes one more argument:

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.other = [1, 2, 3]

    def __deepcopy__(self, memodict={}):
        new_instance = MyClass(self.x, self.y)
        new_instance.__dict__.update(self.__dict__)
        new_instance.x = copy.deepcopy(self.x, memodict)
        new_instance.y = copy.deepcopy(self.y, memodict)
        return new_instance

# It looks very similar to the copy, but the requirement of the extra argument memodict is rooted at what deep copying
# means. Since every object referenced from the initial class has to be recreated, there is a risk of an infinite
# recursion. This can happen if one object somehow references itself. Even if not an infinite recursion loop, you may
# end up copying several times the same data. The memodict is keeping track of the objects already copied. The infinite
# recursion is what we can prevent overwriting the __deepcopy__ method.

# In the example above, what we do is we prevent the deep copy process from generating a new other list. Therefore, we
# end up with a mixed deep copy, in which x and y are really new, while other is the same. If we run the example code,
my_class = MyClass([1, 2], [3, 4])
my_new_class = copy.deepcopy(my_class)

print(id(my_class))  # 139952436046312
print(id(my_new_class))  # 139952436046200

my_class.x[0] = 0
my_class.y[0] = 0
my_class.other[0] = 0
print(my_new_class.x)  # [1, 2]
print(my_new_class.y)  # [3, 4]
print(my_new_class.other)  # [0, 2, 3]

# So, you see now, that .x and .y are unchanged, while .other reflects the changes done on the other class.

#Why defining how to copy
# The simple examples above only show how to achieve different behavior with deep and shallow copies, but they don't
# explain why you would do it. The cases in which you will need to define this custom behavior are not trivial at all.
# Customizing the deep copy would happen if, for instance, the class is holding any kind of cache, and you need to
# preserve it between different objects. Preserving the cache can be useful because you can speed up the code, or
# because it is very large and you don't want to duplicate the memory usage.

# For shallow copies, the use cases are varied. It normally implies that there is at least one attribute that you don't
# want to share between objects. That attribute could be, for instance, the object responsible for communicating with a
# device. You would like to prevent talking at exactly the same time to the same device through the same interface. You
# may also like to protect private attributes, etc.

# Last Warning
# It is very important to point out that, if are worried about copying and deep copying of custom objects, you should
# understand what are mutable and immutable objects in Python, and what are hashable objects. When you have immutable
# data types, such as an integer or a string, all the discussion above doesn't work. If you change an immutable
# attribute in a class, that attribute in deep-copied objects will not change.

# Therefore, the idea of preserving attributes between objects, etc. only works with mutable objects. If you want to
# achieve the behavior of sharing data between objects as a feature, you will need to think how to transform it to
# mutable types or find ways around it.

# Another word of caution goes for people working with multiprocessing. It may be obvious but is never bad to repeat it,
# that sharing data between different processes is not a trivial task and therefore you can't rely on mutable objects to
# share information.