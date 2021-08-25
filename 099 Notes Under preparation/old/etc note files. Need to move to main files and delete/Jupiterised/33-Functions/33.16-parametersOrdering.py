# Make sure that if you use different types o parameters in the same function, order them as follows:
# 1- Parameters
# 2- *args
# 3- default parameters
# 4- **kwargs

def display_info(a, b, *args, instructor="colt", **kwargs):
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3 , last_name="Steele", job="Instructor"))
# [1, 2, (3,), 'colt', {'last_name': 'Steele', 'job': 'Instructor'}]
# arguments have been assigned to the parameters as foolows:
# a - 1
# b - 2
# args (3, ) # NOTE:  if a tuple has a single element, python inserts a comma after it
#              to distinguish it from (3) which is just an int inside brackets
# instructor - "colt"
# kwargs- {last_name:"Steele", job:"Instructor"}

