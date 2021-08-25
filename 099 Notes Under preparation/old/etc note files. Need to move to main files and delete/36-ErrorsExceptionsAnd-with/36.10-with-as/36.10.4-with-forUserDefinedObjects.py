# INTERVIEW REVISION
# TODO https://rszalski.github.io/magicmethods/#context

# Supporting the “with” statement in user defined objects (Context Managers)
# Context managers allow setup and cleanup actions to be taken for objects when their creation is wrapped with a with
# statement. The behavior of the context manager is determined by two magic methods:

# __enter__(self)
# Defines what the context manager should do at the beginning of the block created by the with statement. Note that the
# return value of __enter__ is bound to the target of the with statement, or the name after the as.

# __exit__(self, exception_type, exception_value, traceback)
# Defines what the context manager should do after its block has been executed (or terminates). It can be used to handle
# exceptions, perform cleanup, or do something always done immediately after the action in the block. If the block
# executes successfully, exception_type, exception_value, and traceback will be None. Otherwise, you can choose to
# handle the exception or let the user handle it; if you want to handle it, make sure __exit__ returns True after all is
# said and done. If you don't want the exception to be handled by the context manager, just let it happen.

# __enter__ and __exit__ can be useful for specific classes that have well-defined and common behavior for setup and
# cleanup. You can also use these methods to create generic context managers that wrap other objects.

# Consider the following example for further clarification.

# a simple file writer object
class MessageWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file

    def __exit__(self):
        self.file.close()

        # using with statement with MessageWriter


with MessageWriter('my_file.txt') as xfile:
    xfile.write('hello world')

# - In the code above, what follows the with keyword is the constructor of MessageWriter.
# - As soon as the execution enters the context of the with statement a MessageWriter object is created and python then
#   calls the __enter__() method. In this __enter__() method, initialize the resource you wish to use in the object.
# - This  __enter__() method should always return a descriptor of the acquired resource.

# What are resource descriptors?
# - These are the handles provided by the operating system to access the requested resources. In the following code
#   block, file is a descriptor of the file stream resource ie  file = open('hello.txt')
# - In the MessageWriter example provided above, the __enter__() method creates a file descriptor and returns it. The
#   name xfile here is used to refer to the file descriptor returned by the __enter__() method.
# - The block of code which uses the acquired resource is placed inside the block of the with statement.
# - As soon as the code inside the with block is executed, the __exit__() method is called. All the acquired resources
#   are released in the __exit__() method. This is how we use the with statement with user defined objects.
