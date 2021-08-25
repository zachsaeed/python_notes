# Custom For Loop

# for num in [1,2,3]
# for char in "hi there"


def my_for(iterable, func):
    iterator = iter(iterable)  # get the iterator
    while True:  # continuously loop and call next until break
        try:
            thing = next(iterator)
        except StopIteration:  # When Error raised, means end of iterator. So, break while loop
            break
        else:
            func(thing)  # run passed in function on each item


my_for("lol", print)


def square(x):
    print(x * x)


my_for([1, 2, 3, 4, 5], square)
