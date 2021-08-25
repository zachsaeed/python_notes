# tuples are similar to lists except that
# 1- tuples are immutable
# 2- Created using (items) or tuple( (items) ) function

sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
sample_tuple2 = tuple((1, 2, 3, 4, 5, 6, 7, 8))
print(type(sample_tuple))  # <class 'tuple'>
print(type(sample_tuple2))  # <class 'tuple'>

# Are immutable
# sample_tuple[0] = 1  # TypeError: 'tuple' object does not support item assignment

# Uses:
# Tuples are faster than list
# Used when you have an ordered collection of data that's not going to change. Makes your code safer

# Normally used for unchanging data like
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December')
print(months[-1])  # December

# INTERVIEW
# Note: tuples can be used as valid keys in a dictionary
# https://wiki.python.org/moin/DictionaryKeys
# Here we store location data like latitude and longitude coordinates along with what they represennt
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
  }
print(locations[(35.6895, 39.6917)])  # "Tokyo Office",

# Note: We cannot use lists as dictionary keys as a list is unhashable (Internally hash is used as key)
# locs = {[35.6895, 39.6917]: "Tokyo Office"}  # TypeError: unhashable type: 'list'

# Tuple methods
# There are only 2 tuple methods, index() and count() which are common methods within all sequence types therefore,
# discussed in a separate topic.

# Nested tuples
# you can have nested tuples just like nested lists
