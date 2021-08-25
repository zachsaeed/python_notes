# https://medium.com/@shamir.stav_83310
# https://realpython.com/python-type-checking/

# The docs interchangeably call them type annotations or type hints.
# In other languages, annotations and hints mean something completely different.

# All programming languages include some kind of type system that formalizes which categories of objects it can work
# with and how those categories are treated. For instance, a type system can define a numerical type, with 42 as one
# example of an object of numerical type.

# Dynamic Typing
# Python is a dynamically typed language. This means that the Python interpreter does type checking only as code runs,
# and that the type of a variable is allowed to change over its lifetime.

# Static Typing
# - The opposite of dynamic typing is static typing. Static type checks are performed without running the program. In
#   most statically typed languages, for instance C and Java, this is done as your program is compiled.
# - With static typing, variables generally are not allowed to change types, although mechanisms for casting a variable
#   to a different type may exist.
# - Python will always remain a dynamically typed language. However, pytho 3.5 (PEP 484) introduced type hints, which
#   make it possible to also do static type checking of Python code.
# - Unlike how types work in most other statically typed languages, type hints by themselves don’t cause Python to
#   enforce types. As the name says, type hints just suggest types. There are other tools, which you’ll see later, that
#   perform static type checking using type hints.

# Duck Typing
# - Another term that is often used when talking about Python is duck typing. This moniker comes from the phrase “if it
#   walks like a duck and it quacks like a duck, then it must be a duck” (or any of its variations).
# - Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than
#   the methods it defines. Using duck typing you do not check types at all. Instead you check for the presence of a
#   given method or attribute.
# - See '57.48-ductypingAndDependencyInjection.py'
# - Duck typing is somewhat supported when doing static type checking of Python code, using structural subtyping.

# Type Hints
# Type hints syntax is:
# def function(variable: input_type) -> return_type:
#   pass

# The type annotations are completely optional and are ignored at runtime — meaning two things:
# 1- You can’t break the code by adding them (update: almost — I will elaborate in a future article).
# 2- They have no gain in performance. However, using the typing module will of course have some overhead.
# 3- You may add them only where you see fit — A balanced rule is always annotating function signatures and
#    module-scope variables, but not to bother with local variables.

# Benefits
# 1- We can employ static code analysis to catch type errors prior to runtime— PyCharm does this automatically,
#    highlighting type errors (albeit they are easy to miss in my opinion). Another option, which is definitely
#    recommended, is a useful tool named mypy, which can be run on specific type-annotated files to find type-related
#    errors (I always run it after running my unit tests).
# 2- Cleaner code/the code is self-documenting — as Uncle Bob writes in his (very recommended) book “Clean Code”:
#   “don’t use a comment when you can use a function or a variable”, we can now say “don’t use comments to specify a
#   type (Like in python 2, comments were used to describe variable types), when you can use type annotation”. Comments
#   tend to wear out and rot, while code is alive and must stay fresh. Change the types of the variables without
#   changing the comment specifying the type — nothing happens. Change it without changing the type annotation? Your
#   static analysis tool, whichever it may be, will shout at you.
# 3-
