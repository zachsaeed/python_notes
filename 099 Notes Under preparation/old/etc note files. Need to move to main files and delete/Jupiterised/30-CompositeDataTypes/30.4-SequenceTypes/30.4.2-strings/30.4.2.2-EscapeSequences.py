# String escape characters or Sequences

# In python there are "escape characters" which are "metacharacters" - They get interpreted inside string literals
# by python to do something special (example, ' & " interpreted as start and end of string).

# To suppress the special interpretation of some characters, we use  a backslash (\) in front of those characters. A
# backslash character in a string indicates that one or more characters that follow it should be treated specially.

# Therefore, this is referred to as an escape sequence, because the backslash causes the subsequent character sequence
# to “escape” its usual special meaning.)

msg = 'Hello\nWorld'
print(msg)
# Hello
# World

# A list of all the escape sequences:

# \{newline}       Backslash and newline ignored, where newline is the 'enter' key:
print('a\
b\
c')              # abc

# \\             Backslash (\)
# \'             Single quote (')
# \"             Double quote (")
# \a             ASCII Bell (BEL)
# \b             ASCII Backspace (BS)
# \f             ASCII Formfeed (FF)

# \n             ASCII Linefeed (LF)
print("a\nb")    # a
#                  b

# \N{name}	 Character named 'name' in the Unicode database
print('\N{rightwards arrow}')  # →

# \r             ASCII Carriage Return (CR)
# \t             ASCII Horizontal Tab (TAB)
print("a\tb")    # a	b

# \uxxxx	     Unicode character with 16-bit hex value xxxx. Exactly four hexadecimal digits are required.
print('\u2192')  # →

# \Uxxxxxxxx	 Unicode character with 32-bit hex value xxxxxxxx. Exactly eight hexadecimal digits are required.
# \v             ASCII Vertical Tab (VT)
# \ooo           Character with octal value where ooo represents 3 digits
print("\042")    # a

# \xhh           Character with hex value where hh represents 2 digits
print("\x61")    # a



