# Note: Variables must be assigned before they can be used
# Otherwise you get a name undefined error
# variables
jar = 10;
print(jar)

# can be assigned to other variables
box = jar;
print(box)

# can be reassigned
box = "SAQUIB"
print(box)

# Can be assigned at the ame time as other vars
bottle, case, bag = 'A', 1.5, "Zach"
print(bottle)
print(case)
print(bag)

# We can also use a list to assign each item to variables in a single line
bottle, case, bag = ['A', 1.5, "Zach"]
print(bottle)
print(case)
print(bag)


# Variable naming restrictions

# 1- Must start with a letter or underscore
_cats = 5
cats = 6
# 2cats = 5 #SyntaxError: invalid syntax

# 2- Rest of the name must have letters, numbers or underscores
cats_123 = 10
# cats@gmail = 5 #SyntaxError: can't assign to operator

# 3- Are case sensitive
# CATS != cats


# Python naming conventions

# 1- most variables should be lower_snake_case (not camelCase)
# 2- constants should be CAPITAL_SNAKE_CASE
# 3- class names are UpperCamelCase
# 4- variables that start and end with two underscores 
# (dunder for DoubleUNDERscore) are private or left alone
# __no_touchy__
