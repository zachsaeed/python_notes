# raw Strings
# https://docs.python.org/3/faq/design.html#why-can-t-raw-strings-r-strings-end-with-a-backslash
# A "raw" string literal is prefixed by an 'r' and passes all the chars through without special treatment of
# backslashes, so r'x\nx' evaluates to the length-4 string 'x\nx'.

raw = r'this\t\n and that'
print(raw)  # this\t\n and that

# NOTE: Raw strings are not 100% raw, there is still some rudimentary backslash-processing.
# - More precisely, they can’t end with an odd number of backslashes: the unpaired backslash at the end escapes the
#   closing quote character, leaving an unterminated string.

# Some of the invalid raw strings are:
# print(r'\')  # missing end quote because the end quote is being escaped
# instead:
print(r'\'')  # \'

# print(r'ab\\\')  # first backslash will escape the next, the third one will try to escape the end quote.
# instead:
print(r'ab\\')  # ab\\

raw_s = R'\\\"'  # prefix can be 'R' or 'r'
print(raw_s)  # \\\"


# Formatting Strings
# There are several ways to format a string to interpolate variables

# Using argument specifiers
# Prior to Python 2, the The old way we use argument specifiers % operator (deprecated)
x = 10
formatted = "I've told you %d times already! %s" % (x, "Saeed")
print(formatted)
#  great for simple formatting but limited support for strings, ints, doubles only. We can’t use it with objects.
# Here are some basic argument specifiers you should know:
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)


# Using the format method
# In python 2 to 3.5 we use .format() method
a_var = 10
formatted = "Ive told you {} times already {}".format(a_var, "Saquib")
print(formatted)
# It takes an empty curly brace with the value u need inside format function


# Using f-strings
# In python 3.6+ we use f-strings e.g
x = 10
formatted = f"Ive told you {x} times already"
print(formatted)
# f"{}" takes anything inside the {} and turns it into a string
# we can also do some math in there
print(f"I am {x+20} years older than zach who is {x} years old")
# prefixes can be f'' or F''


# Both f and r can be combined
raw_formatted = fr'this\t\n and that {x}'
print(raw_formatted)  # this\t\n and that 10

# TODO  https://stackoverflow.com/questions/41630728/using-s-vs-s-to-format-a-string-in-python