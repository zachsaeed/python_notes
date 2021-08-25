# Modular programming is the process of breaking a large, unwieldy programming task into separate, smaller, more
# manageable subtasks or modules. Individual modules can then be put together like building blocks to create a larger
# application.
# There are several advantages to modularizing code in a large application:
#
# Simplicity: Rather than focusing on the entire problem at hand, a module typically focuses on one relatively small
# portion of the problem. If you’re working on a single module, then you’ll have a smaller problem domain to wrap your
# head around. This makes development easier and less error-prone.
#
# Maintainability: Modules are typically designed so that they enforce logical boundaries between different problem
# domains. If modules are written in a way that minimizes interdependency, then there is decreased likelihood that
# modifications to a single module will have an impact on other parts of the program. (You may even be able to make
# changes to a module without having any knowledge of the application outside that module.) This makes it more viable
# for a team of many programmers to work collaboratively on a large application.
#
# Reusability: Functionality defined in a single module can be easily reused (through an appropriately defined
# interface) by other parts of the application. This eliminates the need to recreate duplicate code.
#
# Scoping: Modules typically define a separate namespace, which helps avoid collisions between identifiers in different
# areas of a program. (One of the tenets in the Zen of Python is Namespaces are one honking great idea—let’s do more of
# those!)
#
# Functions, modules, and packages are all constructs in Python that promote code modularization.
