# The 'in' and 'not in' keywords are used to check if a value exists in python's built-in composite data types (sequences, sets and
# mapping types) TODO Objects?

# --- Strings:
# It returns a boolean value and is used as below:

# Example strings (Same for list, tuple, byteArray, byte, range, xrange, dictionary, set and frozenset)
demo_string = 'Syed Saquib Saeed'
print('S' in demo_string)  # True
print('Saee' in demo_string)  # True
print('John' in demo_string)  # False

# Example list
demo_list = ['AB', 22, 0.65, 'a']
print('AB' in demo_list)  # True
print(0.65 in demo_list)  # True
print('John' in demo_list)  # False

# Example dictionary:
# We use the 'in' keyword to check for the existence of a certain value in a key or dictionary

my_dictionary = {
    'name': 'Saquib',
    44: 'my favourite number',
    'address': 'chadwell heath',
    'pet': 'cat'
}
# If we access a key that doesnt exist, we get an error
# print(my_dictionary['surname']) # KeyError: 'surname'
# Therefore we can check for existence of keys, before accessing it:
# Note: in is used for checking values in lists, Whereas its used for checking keys in dictionaries
print('name' in my_dictionary)  # True
print('surname' in my_dictionary)  # False

# Note: Its the same as doing:
print('name' in my_dictionary.keys())  # True
# Now to check if a value exists we can do
print('Saquib' in my_dictionary.values())  # True


# practical use
if 'name' in my_dictionary:
    print('There is a name key')
# better use get('keyname', value=None) instead as it is shorter and doesnt need checks for key existence
print(my_dictionary.get('nonExistentKey'))  # None returns the 2nd parameter's default value if key not found
print(my_dictionary.get('nonExistentKey', 100))  # 100 returns the 2nd parameter's value (100) if key not found
print(my_dictionary.get('name'))  # Saquib returns the key's value if key found
print(my_dictionary.get('name', 100))  # Saquib returns the key's value if key found


#sets
# As it doesnt support indexing
# print(s[0]) # TypeError: 'set' object is not subscriptable
# but we can test if an element is in a set:
s={1,2,3,4}
print(2 in s)  # True
print(16 in s)  # False

# dict views
# scroll slightly down
# https://docs.python.org/3.8/library/stdtypes.html#dictionary-view-objects