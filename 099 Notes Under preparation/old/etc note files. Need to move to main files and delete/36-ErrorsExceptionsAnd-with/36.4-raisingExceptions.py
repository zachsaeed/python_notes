# We can raise (throw) our own errors using the raise keyword. This is helpful when
# creating your own kinds of exceptions and error messages

# raise ValueError('invalid value')  # ValueError: invalid value
# raise ValueError  # ValueError

# The code stops and exited as soon as an error is raised
# We can raise any type of error whenever we want but it's good practice to use
# the right type of error.


def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if not isinstance(text, str):
        raise TypeError("text must be instance of str")
    if not isinstance(color, str):
        raise TypeError("color must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print(f"Printed {text} in {color}")


# colorize([], 'cyan')  # TypeError: text must be instance of str
# colorize('34', "red")  # ValueError: color is invalid color
colorize('abc', 'cyan')  # Printed abc in cyan
