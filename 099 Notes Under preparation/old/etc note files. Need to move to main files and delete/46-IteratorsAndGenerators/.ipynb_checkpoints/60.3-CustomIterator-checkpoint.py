# TODO https://rszalski.github.io/magicmethods/#sequence
# For an object to be an iterable, we should be able to call the iter() function on it ie
# it should have a dunder method __iter__() defined in it which will return an iterable
# object
# Similarly, for an object to be an iterator, we should be able to call the next() function
# on it i.e. it should have the dunder method __next__ defined in it which will return an
# element/item from the collection


# Here, the counter object is an iterator and iterable at the same time. ie iter() returns
# self on which you can then call next()

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for x in Counter(50, 70):
    print(x)
