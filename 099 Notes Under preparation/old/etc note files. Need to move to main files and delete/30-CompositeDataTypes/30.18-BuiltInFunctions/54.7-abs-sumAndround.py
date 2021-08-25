# abs(Integer / loating)
# Return he absolute value (he magnitude of a real number without regard to its sign)
# of a number. The argument may be an integer or floating point number

print(abs(5))  # 5
print(abs(-5))  # 5
print(abs(-3.444444))  # 3.444444


# sum(iterable[, start=0])
# Takes an iterable (Except string or string items) and an optional start
# (default 0) which also cannot be a string.
# Returns the total of start and the items of the iterable from let to right
# list
print(sum([1, 2, 3]))  # 6
print(sum([1, 2, 3], -6))  # 0
# tupple
print(sum((1.5, 2, 3)))  # 6.5
# set
print(sum({1, 50, 100}))  # 151

# strings
# print(sum('12345'))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# string items
# print(sum(['hello', 'world']))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(sum(['hello', 'world'], 'everyone'))  # TypeError: sum() can't sum strings [use ''.join(seq) instead]


# round(number, ndigits = 0)
# returns a number rounded to ndigits precision after the decimal point.
# if ndigits is omitted or is None, it returns the nearest integer to its input
print(round(0.5))  # 0
print(round(1.2))  # 1
print(round(1.5))  # 2

# NOTE: Python3 round function uses "banker's rounding" when rounding numbers.
# Python 2's rounding behavior is “round to nearest, ties away from zero.”
# Python 3 uses “round to nearest, ties to nearest even,” sometimes called “banker's rounding.”
# Bankers Rounding is an algorithm for rounding quantities to integers, in which numbers
# which are equidistant from the two nearest integers are rounded to the nearest even integer.
# Thus, 0.5 rounds down to 0; 1.5 rounds up to 2.

print(round(1.212121, 2))  # 1.21
print(round(1.512121, 2))  # 1.51
print(round(1.512121, None))  # 2
# Note:
print(round(1.512121, 0))  # 2.0
print(round(9.999999999999999, 2))  # 10.0   # loses precision here