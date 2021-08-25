# We saw how to create class attributes in the previous section. To access and change a class attribute we could use
# instance methods for this purpose:
class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstances(self):
        return Robot.__counter

x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())

# There are 2 issues here.
# 1- counter has nothing to do with an instance (It is a collective count of instances and should be accessible via
# class)
# 2- To access the counter we need to create an instance

# Possible Solutions:
# If we try to invoke the method with the class name Robot.RobotInstances(), we get an error message, because it needs
# an instance (self) as an argument and we are not accessing it via instance, sel param is not passed:
# print(Robot.RobotInstances())  # TypeError: RobotInstances() takes exactly 1 argument (0 given)

# The next idea, which still doesn't solve our problem, consists in omitting the parameter "self":
class Robot2:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstances():  # we omit 'self' param here
        return Robot2.__counter

# Now it 's possible to access the method via the class name, but we can't call it via an instance:
print(Robot2.RobotInstances())  # 0
x = Robot2()
# print(x.RobotInstances())  # TypeError: RobotInstances() takes 0 positional arguments but 1 was given
# The call "x.RobotInstances()" is treated as an instance method call and an instance method needs a reference to the
# instance as the first parameter.

# We want a method, which we can call via the class name or via the instance name without the necessity of passing a
# reference to an instance to it.

# The solution consists in static methods, which don't need a reference to an instance (self) or a class (cls) as the
# first parameter.
# It's easy to turn a method into a static method. All we have to do is to add a line with "@staticmethod" decorator
# directly on top of the method header. It's the decorator syntax.

# They behave like plain functions except that you can call them from an instance or the class:

class Robot3:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return Robot3.__counter

print(Robot3.RobotInstances())  # 0
x = Robot3()
print(x.RobotInstances())  # 1
y = Robot3()
print(x.RobotInstances())  # 2
print(Robot3.RobotInstances())  # 2

# Static methods are used to create utility functions which have some logical connection to the class as class methods
# dont have access to the instance (via self) or the class (via cls) parameters.
