# Note: when an int and float is added/divided, the result is a float

# Operators
#  +  Addition
#  -  Subtraction
#  *  Multiplication
#  /  Division
#  ** Exponentiation
#  %  Modulo
#  // Integer Division

# INTERVIEW REVISION
# The order of execution of the operators follow PEMDAS and the precedence is:
# Parentheses (simplify inside 'em)
# Exponents
# Multiplication and Division (from left to right)
# Addition and Subtraction (from left to right)


# Exponents are used to calculate the powers or square roots
print(4**2)  # 4 to the power of 2 = 16
print(4**0.5)  # square root of 4

# Modulo gives us the remainder. It keeps on dividing until the remainder is a non fractional number or zero
print(4 % 2)
# Can also be used to find out even odd numbers
print(13 % 2)  # 1 which means odd number
print(14 % 2)  # 0 which means even number

# Integer division (/).
# (//) 'floors' the result ie rounds it down
print(10 / 3)  # 3.33333333... gives us float
print(10 // 3)  # 3 gives us int
print(6 // 7)  # 0 gives us int

# We can also use +=, -=, /= as follows
abc = 10
abc += 10  # is equal to: abc = abc + 10

# rounding floats using round(float to round, how many decimal points)
unrounded_value = float(8) / 1.60934
print(unrounded_value)
rounded_value = round(unrounded_value, 2)
print(rounded_value)


# See: Floating Point Arithmetic: Issues and Limitations
# https://docs.python.org/3.6/tutorial/floatingpoint.html