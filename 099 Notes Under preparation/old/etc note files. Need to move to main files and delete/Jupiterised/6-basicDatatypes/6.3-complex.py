# https://www.youtube.com/watch?v=qcQ7bcpjl9o
# Complex datatypes used in integral algebra and calculus in scientific, mathematical or electrical engineering apps.
# Complex numbers are specified with syntax a+bj ie <real part>+<imaginary part>j. j/J symbol  is compulsory.
# where: square of j = -1
#    or: j = square root of -1

# Real and imaginary can be int or float values
# real ca be int, float, binary, octal or hexadecimal but imaginary must
# always be base 10

var_complex = 2 + 3j
print(var_complex)  # (2+3j)
print(type(2 + 3j))  # <class 'complex'>
print(var_complex.real)  # 2.0  # real part as float
print(var_complex.imag)  # 3.0  # imaginary part as float

# var_complex2 = 2 + 3i  # syntax err
var_complex3 = 2.1 + 3.5j  # real and imag are floats
x = 0B1111 + 20J  # real can be int float binary octal or hexadecimal but imaginary must always be base10 int or float

# We can perform arithmetic operations on complex numbers
print(var_complex + var_complex3)  # (4.1+6.5j)
print(var_complex - var_complex3)  # (-0.10000000000000009-0.5j)
print(var_complex * var_complex3)  # (-6.3+13.3j)
print(var_complex / var_complex3)  # (0.8823529411764707-0.042016806722689114j)
