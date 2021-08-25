# An integer can be declared as
int_var1 = -23
print(type(int_var1))  # <class 'int'>

int_var2 = int(23)
print(type(int_var2))  # <class 'int'>

# Size: There is effectively no limit to how long an integer value can be. Of course, it is constrained by the amount
# of memory your system has, as are all things, but beyond that an integer can be as long as you need it to be:
import sys
int_var1 = 0
print(sys.getsizeof(int_var1))  # 24

int_var2 = 123123123123123123123123123123123123123123123124
print(sys.getsizeof(int_var2))  # 48

# base 10 (Decimal)
# Python interprets a sequence of decimal digits without any prefix to be a decimal number by default
int_var_base10 = 10
print(int_var_base10)  # 10

# base 2 (Binary): To define an integer as binary we prepend 0b (zero + 'b' or 'B')
int_var_base2 = 0b10
print(int_var_base2)  # 2

# base 8 (Octal): To define an integer as Octal we prepend 0o (zero + 'o' or 'O')
int_var_base8 = 0o10
print(int_var_base8)  # 8

# base 16 (Hexadecimal): To define an integer as hexadecimal we prepend 0x (zero + 'x' or 'X')
int_var_base16 = 0x10
print(int_var_base16)  # 16

# Note: The underlying type, irrespective of the base used to specify it, will be int
