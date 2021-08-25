# Python has a built-in string class named "str" with many handy features
# (Note: there is an older module named "string" which you should not use).

# Python strings are "immutable" which means they cannot be changed after they are created. Since strings can't be
# changed, we construct *new* strings as we go to represent computed values.
# So for example the expression ('hello' + 'there') takes in the 2 strings 'hello' and 'there' and builds a new
# string 'hellothere'.

# A string in Python can contain as many characters as you wish. The only limit is your machine’s memory resources.

# Strings can be created using the class str or many other ways which are shorter
name = str('Syed')
print(name)  # Syed
print(type(name))  # <class 'str'>



# String literals may be delimited using either single or double quotes. All the characters between the opening
# delimiter and matching closing delimiter are part of the string. Therefore, If you want to include either type of
# quote character within the string, the simplest way is to delimit the string with the other type.
name1 = "Sa'q'uib"
print(name1)  # Sa'q'uib

name2 = 'Sa"eed'
print(name2)  # Sa"eed

# A string can also be empty:
name3 = ''
print(name3)   #


# Multiline string literals:
# A string literal can span multiple lines, but there must be a backslash \ at the end of each line to escape the
# newline and concatenate the lines.
multi = 'It was the best of times.'\
    'It was the worst of times.'\
    'Hello brother'
print(multi)  # It was the best of times.It was the worst of times.Hello brother

# String literals inside triple quotes, """ or ''', can span multiple lines of text
multi2 = '''It was the best of times.
    It was the worst of times.
    Hello brother'''
print(multi2)
# It was the best of times.
#     It was the worst of times.
#     Hello brother
