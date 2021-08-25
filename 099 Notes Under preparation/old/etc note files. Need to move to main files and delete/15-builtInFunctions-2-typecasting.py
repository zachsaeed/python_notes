# In python we convert datatypes from one to the other so that they are easier to work with

# -- Python Implicit Data Type Conversion
# Implicit conversion or coercion is when data type conversion takes place either during compilation or during run time
# and is handled directly by Python for you.
a_int = 1
b_float = 1.0
c_sum = a_int + b_float
print(c_sum)  # 2.0
print(type(c_sum))  # <class 'float'>  # you can use the type() function in Python to check the data type of an object.
# Above, the result was automatically converted to a float value c_sum without you having to tell the compiler.
# This is the implicit data conversion.

# NOTE: This is due to a broader concept of type promotion in computer science. Simply put, this is a defense mechanism
# of the compiler that allows you to perform operations whenever possible by converting your data into a different
# supertype without the loss of information.
# That means that the conversion from float to integer is not done because then the compiler will need to remove the
# fractional part leading to the loss of information.


# -- Python Explicit Data Type Conversion
# Explicit conversion also known as type casting is when data type conversion takes place because you clearly defined
# it in your program.
# You basically force an expression to be of a specific type. The general form of an explicit data type conversion is
# as follows:   <required_data_type>(expression)

# we have the following builtin methods which we use for type conversion or related to it:
# ascii()	Returns a string containing a printable representation of an object
# bin()	Converts an integer to a binary string
# bool()	Converts an argument to a Boolean value
# chr()	Returns string representation of character given by integer argument
# unichr() Returns string representation of unicode character given by integer argument
# complex()	Returns a complex number constructed from arguments
# float()	Returns a floating-point object constructed from a number or string
# hex()	Converts an integer to a hexadecimal string
# int()	Returns an integer object constructed from a number or string
# oct()	Converts an integer to an octal string
# ord()	Returns integer representation of a character (character can be unicode or ASCII)
# repr()	Returns a string containing a printable representation of an object
# str()	Returns a string version of an object
# type()	Returns the type of an object or creates a new type object


# Note: as you can imagine, with explicit data type conversion, there is a risk of information loss since you're
# forcing an expression to be of a specific type.

# Recap: Primitive data structures are the building blocks for data manipulation and contain pure, simple values of
# data. Python has four primitive variable types:
# Integers
# Float
# Strings
# Boolean
# Non-primitive data structures don't just store a value, but rather a collection of values in various formats. In
# Python, you have the following non-primitive data structures:
# Lists
# Tuples
# Dictionary
# Sets

# -- Integer and Float Conversions
# Integers and floats are data types that deal with numbers.
# To convert the integer to float, use the float() function in Python. Similarly, if you want to convert a float to an
# integer, you can use the int() function.
a_int = 3
b_int = 2
# Explicit type conversion from int to float
c_float_sum = float(a_int + b_int)
print(c_float_sum)  # 5.0

a_float = 3.3
b_float = 2.0
# Explicit type conversion from float to int
c_int_sum = int(a_float + b_float)
print(c_int_sum)  # 5    # 0.3 is lost
c_float_sum = a_float + b_float
print(c_float_sum)  # 5.3

# -- Data Type Conversion with Strings
# A string is a collection of one or more characters (letters, numbers, symbols). You may need to convert strings to
# numbers or numbers to strings fairly often. You can do this using the str() function:
price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
# print("The total is: " + total + "$")  # TypeError: Can't convert 'int' object to str implicitly
# The example above gives a TypeError, informing that the compiler cannot implicitly convert an integer value to a
# string.

# It might seem intuitive to you what the program should do here. However, the compiler might not always be sure, and
# that's why it provides a mechanism with the explicit type casting so that you can clearly state what you want.
# Let's see the same example with type casting:
price_cake = 15
price_cookie = 6
total = price_cake + price_cookie
print("The total is: " + str(total) + "$")  # The total is: 21$
# It works the same way when you convert float to string values.

# In Python, you can also convert strings to integer and float values whenever possible. Let's see what this means:
price_cake = '15'
price_cookie = '6'
# String concatenation
total = price_cake + price_cookie
print("The total is: " + total + "$")  # The total is: 156$
# Explicit type conversion to integer
total = int(price_cake) + int(price_cookie)
print("The total is: " + str(total)  + "$")  # The total is: 21$
# price_cake and price_cookie are initially strings. Then, you need to find the total, which means they have to be
# first converted to their corresponding integer values. Else, the compiler will assume the operation that you want
# is a string concatenation rather than a numerical addition. You then need to put this value into the final display
# string and consequently need to convert the total to a string so as to concatenate it with the rest of the display
# message.

# Note: did you notice the "whenever possible" when trying to convert a string to integers or float? This is because
# it is not always possible to convert strings to numbers and apply numerical operations on them. The compiler is aware
# of this and will, therefore, give you an error when you try to do so. Check out the example below:
price_cake = 'fifteen'
price_cookie = 'six'
# total = int(price_cake) + int(price_cookie)  # ValueError: invalid literal for int() with base 10: 'fifteen'

# -- Type Conversion to Tuples and Lists (more later in the course)
# Just like with integers and floats, you can also convert lists to tuples and tuples to lists.
# Remember what tuple and lists are? Lists and Tuples in Python are used to store a collection of homogeneous items. The
# difference between tuples and list is that tuples are immutable, which means once defined you cannot delete, add or
# edit any values inside it.
# - Why would you convert lists to tuples?
# That's because tuples are immutable data type and allows substantial optimization to the programs that you create.
# - And why would you convert tuples to lists?
# Maybe you want to make changes to the initial tuple. Thus, you can convert them to lists and then make the change,
# then convert them back to tuples.

# You can use the tuple() function to return a tuple version of the value passed to it and similarly the list()
# function to convert to a list:
a_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b_list = [1, 2, 3, 4, 5]
print(tuple(b_list))  # (1, 2, 3, 4, 5)
print(list(a_tuple))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# You can also convert a string into a list or a tuple.
dessert = 'Cake'
# Convert the characters in a string to individual items in a tuple
print(tuple(dessert))  # ('C', 'a', 'k', 'e')
# Convert a string into a list
dessert_list = list(dessert)
dessert_list.append('s')
print(dessert_list)  # ['C', 'a', 'k', 'e', 's']


# -- Binary, Octal, and Hexadecimal Integers in Python
# The number systems refer to the number of symbols or characters used to represent any numerical value. The number
# system that you typically use every day is called decimal. In the decimal system, you use ten different symbols:
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9. With these ten symbols, you can represent any quantity.
# Binary, hexadecimal, and octal refer to different number systems.

# When you run out of symbols, you go to the next digit placement. In the decimal system, to represent one higher than
# 9, you use 10 meaning one unit of ten and zero units of one. However, it is different in other number systems. For
# example, when you consider a binary system which only uses two symbols: 0 and 1, when you run out of symbols, you
# need to go to the next digit placement. So this is how you will count in binary: 0, 1, 10, 11, 100, 101 and so on.

# -- Convert to Binary Number
# Binary integers are the number represented with base two. Which means in the binary number system, there are only
# two symbols used to represent numbers: 0 and 1. When you count up from zero in binary, you run out of symbols more
# quickly: 0, 1, ???
# Furthermore, there are no more symbols left. You do not go to the digit 2 because 2 doesn't exist in binary. Instead,
# you use a special combination of 1s and 0s. In a binary system, 1000 is equal to 8 in decimal. In binary, you use
# powers of two, which means 8 is basically: (1(2^3)) + (0(2^2)) + (0(2^1)) + (0(2^0))= 8. The position of the 1 and 0
# defines the power to which 2 is to be raised to.

# Let's see this with a more complex example to make it clear:
# Binary Number = 1001111
# Decimal value = (1*(2^6)) + (0*(2^5)) + (0*(2^4)) + (1*(2^3)) + (1*(2^2)) + (1*(2^1)) + (1*(2^0))
#               = 79
# In Python, you can simply use the bin() function to convert from a decimal value to its corresponding binary value.
# And similarly, the int() function to convert a binary to its decimal value. The int() function takes as second
# argument the base of the number to be converted, which is 2 in case of binary numbers.

a = 79
# Base 2(binary)
bin_a = bin(a)
print(bin_a) # # 0b1001111
# NOTE:
print(int(bin_a, 2))  # 79  # converts back to decimal where 2 represents Base 2(binary)

# -- Conversion to Octal
# Octal is another number system with fewer symbols to use than the conventional decimal number system. Octal is base
# eight, which means that eight symbols are used to represent all the quantities. They are 0, 1, 2, 3, 4, 5, 6 and 7.
# After 7 is 10, since 8 doesn't exist.
# Just like you used powers of two in binary to determine the value of a number, you will use powers of 8 since this is
# base eight.
# In a binary system, 10 is equal to 8 in octal. Let's break it down: (1(8^1)) + (0(8^0))= 8.
# A more complex example:
# Octal Number = 117
# Decimal value = (1*(8^2)) + (1*(8^1)) + (7*(8^0))
#               = 79
# In Python, you can use the oct() function to convert from a decimal value to its corresponding octal value.
# Alternatively, you can also use the int() function along with the correct base which is 8 for the octal number system.
a = 79
# Base 8(octal)
oct_a = oct(a)
print(oct_a)  # 0o117
print(int(oct_a, 8))  # 79

# -- Type conversion to Hexadecimal
# Hexadecimal is a base 16 number system. Unlike binary and octal, hexadecimal has six additional symbols that it used
# beyond the numbers found in the decimal number system.
# But what comes after 9?
# Once additional symbols are needed beyond the normal numerical values, letters are to be used. So in hexadecimal, the
# total list of symbols used is: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  A,  B,  C,  D,  E and  F.
# which is equal to     Decimal: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 and 15.
# Using the same example as earlier:
# Hexadecimal Number = 4F
# Decimal value = (4*(16^1)) + (15*(16^0))     # where F represents 15
#               = 79
# In Python, you can use the hex() function to convert from a decimal value to its corresponding hexadecimal value, or
# the int() function with base 16 for the hexadecimal number system.

a = 79
# Base 16(hexadecimal)
hex_a = hex(a)
print(hex_a)  # 0x4f
print(int(hex_a, 16))  # 79


# Note: Never used str, int, float as a variable name as its a reserved keyword and used for typecasting
int = "I am a number"  # This is allowed as a variable name can be anything
# Because, now if we use int for typecasting, it will throw an error as int is already used as a var name
# a_var = int(9.4)  # TypeError: 'str' object is not callable


# -- ASCII number to character and character to ASCII
# Get the ASCII number of a character. Accepts unicode too
char = 'a'
number = ord(char)
print(number)  # 97

# Get the character given by an ASCII number
number = 97
char = chr(number)
print(char)  # a

# For unicode we use unichr()
