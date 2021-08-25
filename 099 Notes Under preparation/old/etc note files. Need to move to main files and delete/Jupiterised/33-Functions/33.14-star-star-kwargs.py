# **kwargs or key-word-args

# used in function param list like *args
# gathers remaining keyword arguments as a dictionary
# can be called whatever we want

def fav_colors(**kwargs):
    #kwargs needs to be treated as a dictionary here
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)  # {'colt': 'purple', 'ruby': 'red', 'ethel': 'teal'}
    for k,v in kwargs.items():
        print(f"{k}'s favourite color is {v}")
        # colt's favourite color is purple
        # ruby's favourite color is red
        # ethel's favourite color is teal

fav_colors(colt='purple', ruby='red', ethel='teal')

