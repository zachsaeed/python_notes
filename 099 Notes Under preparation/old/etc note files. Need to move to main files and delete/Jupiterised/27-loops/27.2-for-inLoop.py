# Format

# for item in iterable_object:
# 	 do something with item

# iterable_object is some kind of collection of items, for instance, a 
# list of numbers, a string of characters, a range etc

# item is a new variable that can be called whatever you want

# item references the current position of our iterator within the iterable.
# It will iterate over (run through) every item of the collection and then
# go away when it has visited all items

for char in "hello":
	print(char)

x = range(3, 6)
for n in x:
  print(n)

