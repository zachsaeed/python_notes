# --------- Creating Nan and Inf objects:
#
# In all versions of Python, we can represent infinity and NaN ("not a number") as follows:
# ╒══════════╤══════════════╤════════════════════╤════════════════════╤═══════════════════════════════════════════════╕
# │   result │ NaN          │ inf                │ -Inf               │                                               │
# │ module   │              │                    │                    │                                               │
# ╞══════════╪══════════════╪════════════════════╪════════════════════╪═══════════════════════════════════════════════╡
# │          │              │ float("infinity")  │ -float("infinity") │ We can use +inf, iNf, infinity, +infinity,    │
# │ built-in │ float("nan") │ float("inf")       │ -float("inf")      │ InFiNiTy, an, NaN, NAN etc as it is case      │
# │          │              │ float("+inf")      │ float("-inf")      │ insensitive                                   │
# │          │              │ float("+infinity") │ float("-infinity") │                                               │
# ├──────────┼──────────────┼────────────────────┼────────────────────┼───────────────────────────────────────────────┤
# │ math     │ math.nan     │ math.inf           │ -math.inf          │                                               │
# │          │              │                    │                    │                                               │
# ├──────────┼──────────────┼────────────────────┼────────────────────┼───────────────────────────────────────────────┤
# │ cmath    │ cmath.nan    │ cmath.inf          │ -cmath.inf         │ cmath is the maths library for complex numbers│
# │          │              │                    │                    │ The cmath and numpy constants return plain    │
# │          │              │                    │                    │ Python float objects.                         │
# ├──────────┼──────────────┼────────────────────┼────────────────────┼───────────────────────────────────────────────┤
# │ numpy    │ numpy.nan    │ numpy.PINF         │ numpy.NINF         │ The numpy.NINF is actually the only constant I│
# │          │ numpy.NaN    │ numpy.inf          │ -numpy.inf         │ know of that doesn't require the -            │
# │          │ numpy.NAN    │ numpy.infty        │ -numpy.infty       │  The cmath and numpy constants return plain   │
# │          │              │ numpy.Inf          │ -numpy.Inf         │  Python float objects.                        │
# │          │              │ numpy.Infinity     │ -numpy.Infinity    │                                               │
# ╘══════════╧══════════════╧════════════════════╧════════════════════╧═══════════════════════════════════════════════╛

# It is also possible to create complex NaN and Infinity with complex and cmath:
# ╒═════════╤══════════════╤═══════════════╤═══════════════════╤════════════════════╤══════════════════════════════════╕
# │ result  │ NaN+0j       │ 0+NaNj        │ Inf+0j            │ 0+Infj             │                                  │
# │ module  │              │               │                   │                    │                                  │
# ╞═════════╪══════════════╪═══════════════╪═══════════════════╪════════════════════╪══════════════════════════════════╡
# │built-in │complex("nan")│complex("nanj")│complex("inf")     │complex("infj")     │                                  │
# │         │              │               │complex("infinity")│complex("infinityj")│                                  │
# ├─────────┼──────────────┼───────────────┼───────────────────┼────────────────────┼──────────────────────────────────┤
# │ cmath   │ cmath.nan ¹  │cmath.nanj     │cmath.inf ¹        │cmath.infj          │                                  │
# ╘═════════╧══════════════╧═══════════════╧═══════════════════╧════════════════════╧══════════════════════════════════╛
# The options with ¹ return a plain float, not a complex.

# Function to check whether a number is nan, infinite or finite:
# ╒═══════╤═══════════╤═══════════╤═════════════════╤══════════════════════════════════════════════════════════════════╕
# │ for   │NaN        │Infinity or│not NaN and      │                                                                  │
# │       │           │-Infinity  │not Infinity and │                                                                  │
# │module │           │           │not -Infinity    │                                                                  │
# │       │           │           │                 │                                                                  │
# ╞═══════╪═══════════╪═══════════╪═════════════════╪══════════════════════════════════════════════════════════════════╡
# │math   │math.isnan │math.isinf │math.isfinite    │- math.isnan does not work with complex numbers. Use              │
# │       │           │           │                 │- math.isnan(x.real) or math.isnan(x.imag) instead                │
# ├───────┼───────────┼───────────┼─────────────────┼──────────────────────────────────────────────────────────────────┤
# │cmath  │cmath.isnan│cmath.isinf│cmath.isfinite   │- The cmath and numpy functions also work for complex objects they│
# │       │           │           │                 │will check if either real or imaginary part is NaN or Infinity.   │
# │       │           │           │                 │                                                                  │
# ├───────┼───────────┼───────────┼─────────────────┼──────────────────────────────────────────────────────────────────┤
# │numpy  │numpy.isnan│numpy.isinf│numpy.isfinite   │- The cmath and numpy functions also work for complex objects they│
# │       │           │           │                 │will check if either real or imaginary part is NaN or Infinity .  │
# │       │           │           │numpy.isposinf   │- The numpy functions also work for numpy arrays and everything   │
# │       │           │           │                 │can be converted to one (like lists, tuple, etc.)                 │
# │       │           │           │numpy.isneginf   │- There are also functions that explicitly check for positive and │
# │       │           │           │                 │negative infinity in NumPy:  and numpy..                          │
# ╘═══════╧═══════════╧═══════════╧═════════════════╧══════════════════════════════════════════════════════════════════╛

import math, sys

pos_inf = float('inf')     # +ve infinity (Can use +inf, iNf, infinity, +infinity, InFiNiTy) is case insensitive
neg_inf = float('-inf')    # -ve infinity (Can use -inf, -iNf, -infinity, -InFiNiTy or -float('inf') is case insensitive
not_a_num = float('nan')   # not a number (Can use nan, NaN, NAN etc us case insensitive)


# ------- Comparision Operators
# Although positive and negative infinity can be said to be symmetric about 0 ie -inf < 0 < inf
print(pos_inf > 0)  # True
print(neg_inf < 0)  # True
print(pos_inf > neg_inf)  # True

# We can test specifically for positive infinity or for negative infinity by direct comparison:
print(pos_inf == float('inf'))  #  True  # or  == math.inf
print(neg_inf == float('-inf'))  #  True  # or  == -math.inf
print(neg_inf == pos_inf)  # False

# Comparison operators work as expected for positive and negative infinity:
print(sys.float_info.max)  # 1.7976931348623157e+308  (this is system-dependent)

print(pos_inf > sys.float_info.max)  # True
print(neg_inf < -sys.float_info.max)  # True

# But if an arithmetic expression produces a value larger than the maximum that can be represented as a float, it will
# become infinity:
print(pos_inf == sys.float_info.max * 1.0000001)  # True
print(neg_inf == -sys.float_info.max * 1.0000001)  # True


# -- nan Comparisions:
# When comparing operations, all returned are False, even if the two floats ('nan') are equal to each other.
print(float('nan') > float('inf'))  # False
print(float('nan') > float('-inf'))  # False
print(float('nan') < float('inf'))  # False
print(float('nan') < float('-inf'))  # False
# Note: NaN is never equal to anything, not even itself.
print(float('nan') == float('nan'))  # False

# NaN always compares as "not equal", but never less than or greater than:
print(float('nan') != float('nan'))  # True
print(not_a_num != 5.0)    # or any random value  # True
print(not_a_num > 5.0   or   not_a_num < 5.0   or   not_a_num == 5.0)  # False


# ---------- Arithmetic Operations:
# Arithmetic operations on infinity just give infinite results, or sometimes NaN:

# Positive infinite float('inf')
print(float('inf') + 100)  # inf
print(float('inf') - 100)  # inf
print(float('inf') * 100)  # inf
print(float('inf') / 100)  # inf
print(float('inf') + float('inf'))  # inf
print(float('inf') - float('inf'))  # nan
print(float('inf') * float('inf'))  # inf
print(float('inf') / float('inf'))  # nan
print(100 + float('inf'))  # inf
print(100 - float('inf'))  # -inf
print(100 * float('inf'))  # inf
print(100 / float('inf'))  # 0.0

# Negative infinite float('inf')
print(float('-inf') + 100)  # -inf
print(float('-inf') - 100)  # -inf
print(float('-inf') * 100)  # -inf
print(float('-inf') / 100)  # -inf
print(float('-inf') + float('-inf'))  # -inf
print(float('-inf') - float('-inf'))  # nan
print(float('-inf') * float('-inf'))  # inf
print(float('-inf') / float('-inf'))  # nan
print(100 + float('-inf'))  # -inf
print(100 - float('-inf'))  # inf
print(100 * float('-inf'))  # -inf
print(100 / float('-inf'))  # -0.0
# It can be seen above that positive infinite float('inf') and negative infinite float('inf') operations have the same
# advantages and disadvantages.

# Operations between positive infinite float('inf') and negative infinite float('inf'):
print(float('inf') + float('-inf'))  # nan
print(float('inf') - float('-inf'))  # inf
print(float('-inf') - float('inf'))  # -inf
print(float('inf') * float('-inf'))  # -inf
print(float('inf') / float('-inf'))  # nan
print(float('-inf') / float('inf'))  # nan

# However division by zero does not give a result of infinity (or negative infinity where appropriate), rather it raises
# a ZeroDivisionError exception.
print('Division by zero error is thrown:')
try:
    x = pos_inf / 0.0  # same with: x = 100 / 0.0
    print(x)
except ZeroDivisionError:
    print("Division by zero")   # Division by zero


# All Arithmetic operations involving Nan return nan. This includes multiplication by -1: there is no "negative NaN".
print(float('nan') + 100)  # nan
print(float('nan') - 100)  # nan
print(float('nan') * 100)  # nan
print(float('nan') / 100)  # nan
print(float('-nan'))  # nan
print(-math.nan)  # nan

# There is one subtle difference between the old float versions of NaN and infinity and the Python 3.5+ math library
# constants: please see bottom on page: https://programmer.ink/think/inf-and-nan-in-python.html
print(math.inf is math.inf, math.nan is math.nan)  # True, True since they are the same objects everytime theyre called
print(float('inf') is float('inf'), float('nan') is float('nan'))  # False, False because they are different objects
print(math.inf is float('inf'), math.nan is float('nan'))  # False, False because they are different objects


# -------- Is it possible to set an element of an array to NaN in Python?
# In a list it's no problem, you can always include NaN (or Infinity) there:
a_list = [math.nan, math.inf, -math.inf, 1]  # python list
print(a_list)  # [nan, inf, -inf, 1]

# However if you want to include it in an array (for example array.array or numpy.array) then the type of the array must
# be float or complex because otherwise it will try to downcast it to the arrays type!
# import numpy as np
# float_numpy_array = np.array([0., 0., 0.], dtype=float)
# float_numpy_array[0] = float("nan")
# print(float_numpy_array)  # array([nan,  0.,  0.])

import array
float_array = array.array('d', [0, 0, 0])
float_array[0] = float("nan")
print(float_array)  # array('d', [nan, 0.0, 0.0])

# integer_numpy_array = np.array([0, 0, 0], dtype=int)
# integer_numpy_array[0] = float("nan")  # ValueError: cannot convert float NaN to integer
