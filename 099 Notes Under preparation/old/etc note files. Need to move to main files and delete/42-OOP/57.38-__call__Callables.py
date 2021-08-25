# The __call__ method enables Python programmers to write classes where the
# instances behave like functions. Both functions and the instances of such
# classes are called callables.


class Foo:
    def __call__(self, a, b, c):
        pass


x = Foo()
x(1, 2, 3) # __call__

# TODO: uses of call
