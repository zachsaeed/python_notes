# Here, we create a decoator that enforces what argument datatypes are allowed
# when a function is called


def enforce(*types):  # Decorator that takes any number of arguments
    def decorator(f):  # Actual decorator (inner function) as we need argument support for our decorator
        def new_func(*args, **kwargs):  # wrapper function
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
                # feel free to have more elaborated conversion:
                newargs.append(t(a))  # cast each argument with type.
            return f(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    print(a / b)


# repeat_msg("hello", '5')
divide('1', '4')
