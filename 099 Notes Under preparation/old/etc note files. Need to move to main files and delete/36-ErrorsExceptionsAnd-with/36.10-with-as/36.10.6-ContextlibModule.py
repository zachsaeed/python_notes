# INTERVIEW REVISION
# Here, we require the knowledge of generators, decorators and yield.

# The contextlib module
# https://docs.python.org/3/library/contextlib.html
# A class based context manager as shown previously is not the only way to support the with statement in user defined
# objects. The contextlib module provides a few more abstractions built upon the basic context manager interface. Here
# is how we can rewrite the context manager for the MessageWriter object
# using the contextlib module


from contextlib import contextmanager

class MessageWriter(object):
    def __init__(self, filename):
        self.file_name = filename

    @contextmanager
    def open_file(self):
        try:
            file = open(self.file_name, 'w')
            yield file
        finally:
            file.close()


# usage
message_writer = MessageWriter('hello.txt')
with message_writer.open_file() as my_file:
    my_file.write('hello world')


# - In this code example, because of the yield statement in its definition, the function open_file() is a generator
#   function.
# - When this open_file() function is called, it creates a resource descriptor named file. This resource descriptor is
#   then passed to the caller and is represented here by the variable my_file. After the code inside the with block is
#   executed the program control returns back to the open_file() function. The open_file() function resumes its
#   execution and executes the code following the yield statement. This part of code which appears after the yield
#   statement releases the acquired resources. The @contextmanager here is a decorator.

# The previous class-based implementation and this generator-based implementation of context managers is internally the
# same. While the later seems more readable, it requires the knowledge of generators, decorators and yield.
