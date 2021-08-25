# The logical operators are used to make boolean Logic comparisons or statements
# and    -Truthy if both a AND b are true (Logical conjunction)
# or     -Truthy if either a OR b are true (Logical disjunction)
# NOT    -Truthy of the opposite of a is true (Logical Negation)

# logical 'and'
# In 'and', both conditions need to be True to get True. Otherwise returns
# False
print(True and True)  # True
print(False and True)  # False
print(False and False)  # False


age = input('what is your age?')
if int(age) > 2 and int(age) < 8:
    print('you pay the child price')
else:
    print('you pay the adult price')

# logical 'or'
# In 'or', just one or both conditions need be True to get True. Otherwise
# returns False
print(True or False)  # True
print(True or True)  # True
print(False or False)  # False

city = input('where do you live?')
if city == 'los angeles' or city == 'san francisco':
    print('you live in california')
else:
    print('you dont live in california')

# logical 'not'
# In 'not' it just takes a single boolean and opposites it
print(not False)  # True
print(not True or False)  # False
print(not False and True)  # True

age = input('what is your age?')
# 2-4 $2 ticket
# 68 or greater $5 ticket
# $10 for everyone else
if not( (int(age) >= 2 and int(age) <= 8) or int(age) >= 65 ):
    print('you pay $10 and are not a child or senior')
else:
    print('you are a child or senior')
