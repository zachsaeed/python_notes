# Length of string:
s = "Syed Saquib Saeed"
print(len(s))  # 17

# Here are some of the most common string methods. A method is like a function, but it runs "on" an object.

# index() and count() which are common methods within all sequence types therefore, discussed in a separate topic.


# s.find('other')
# -- searches for the given other string (not a regular expression) within s, and returns the first index where it
# begins or -1 if not found (Same as index() except that find() returns -1 if not found)


# s.lower(), s.upper()
# -- returns the 'lowercase' or 'UPPERCASE' version of the string


# s.strip()
# -- returns a string with whitespace removed from the start and end


# s.isalpha()/s.isdigit()/s.isspace()...
# -- tests if all the string chars are in the various character classes


# s.startswith('other'),   s.endswith('other')
# -- tests if the string starts or ends with the given other string


# s.replace('old', 'new')
# -- returns a string where all occurrences of 'old' have been replaced by 'new'


# s.split('delim')
# -- returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's
# just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no
# arguments) splits on all whitespace chars.
print('s,a,q,u,i,b'.split(','))  # ['s', 'a', 'q', 'u', 'i', 'b']
print('ssadassqsdssuasdasssiasdasssb'.split('ss'))  # ['', 'ada', 'qsd', 'uasda', 'siasda', 'sb']

# s.join(list)
# -- opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g.
# '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
words = ['Coding', 'is', 'fun']
print(' '.join(words))  # Coding is fun
print('--'.join(words))  # Coding--is--fun
