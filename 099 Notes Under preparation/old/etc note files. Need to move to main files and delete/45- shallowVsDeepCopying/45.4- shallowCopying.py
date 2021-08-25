# Shallow Copying:
# Let’s look at some examples to drive home this difference between deep and shallow copies.

print('Making Shallow Copies')
# In the example below, we’ll create a new nested list and then shallowly copy it with the list() factory function:
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = list(xs)  # Make a shallow copy
# This means ys will now be a new and independent object with the same contents as xs. You can verify this by inspecting
# the id of both objects:
print(id(xs))  # 4428671728
print(id(ys))  # 4428691008

# To confirm ys really is independent from the original, let’s devise a little experiment. You could try and add a new
# sublist to the original (xs) and then check to make sure this modification didn’t affect the copy (ys):
xs.append(['new sublist'])
print(xs)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['new sublist']]
print(ys)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# As you can see, this had the expected effect. Modifying the copied list at a “superficial” level was no problem at
# all.

# However, because we only created a shallow copy of the original list, ys still contains references to the original
# child objects stored in xs.
print(id(xs[0]))  # 4459240416
print(id(ys[0]))  # 4459240416
# These children were not copied. They were merely referenced again in the copied list.

# Therefore, when you modify one of the child objects in xs, this modification will be reflected in ys as well—that’s
# because both lists share the same child objects. The copy is only a shallow, one level deep copy:
xs[1][0] = 'X'
print(xs)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9], ['new sublist']]
print(ys)  # [[1, 2, 3], ['X', 5, 6], [7, 8, 9]]
# In the above example we (seemingly) only made a change to xs. But it turns out that both sublists at index 1 in xs and
# ys were modified. Again, this happened because we had only created a shallow copy of the original list.

print('Making shallow copies using the copy module:')
# By the way, you can also create shallow copies using a function in the copy module. The copy.copy() function creates
# shallow copies of objects.
import copy
xs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ys = copy.copy(xs)  # Make a shallow copy
print('proves its a copy:')
print(id(xs))  # 4320347872
print(id(ys))  # 4320328432
print('proves its a shallow copy:')
print(id(xs[0]))  # 4388154096
print(id(ys[0]))  # 4388154096

# This is useful if you need to clearly communicate that you’re creating a shallow copy somewhere in your code. Using
# copy.copy() lets you indicate this fact. However, for built-in collections it’s considered more Pythonic to simply use
# the list, dict, and set factory functions to create shallow copies.


