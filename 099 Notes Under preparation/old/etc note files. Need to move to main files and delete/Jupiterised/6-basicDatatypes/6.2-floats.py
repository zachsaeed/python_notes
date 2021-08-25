# syntax: float([x])  Return a floating point number constructed from a number or string x.
# The float type in Python designates a floating-point number. float values are specified with a decimal point.
# Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific
# notation:
var1 = -23.
print(type(var1))  # <class 'float'>

var2 = float(1.8e308)
print(type(var2))  # <class 'float'>

# Size: The size of a float is always 24 bits
import sys
var1 = .0
print(sys.getsizeof(var1))  # 24

var2 = 1.8e308
print(sys.getsizeof(var2))  # 24


# Deep Dive: Floating-Point Representation
# Almost all platforms represent Python float values as 64-bit “double-precision” values, according to the IEEE 754
# standard. In that case, the maximum value a floating-point number can have is approximately 1.8 ⨉ 10^308.
# Python will indicate a number greater than that by the string inf:
print(1.79e308)  # 1.79e+308
print(1.8e308)  # inf


# The closest a nonzero number can be to zero is approximately 5.0 ⨉ 10^-324. Anything closer to zero than that is
# effectively zero:
print(5e-324)  # 5e-324
print(1e-325)  # 0.0

# Floating point numbers are represented internally as binary (base-2) fractions. Most decimal fractions cannot be
# represented exactly as binary fractions, so in most cases the internal representation of a floating-point number is an
# approximation of the actual value. In practice, the difference between the actual value and the represented value is
# very small and should not usually cause significant problems.

# Further reading:
# Floating Point Arithmetic: Issues and Limitations: https://docs.python.org/3.6/tutorial/floatingpoint.html

# Working with Inf and Nan:
abc = float('Inf')
print(abc)
