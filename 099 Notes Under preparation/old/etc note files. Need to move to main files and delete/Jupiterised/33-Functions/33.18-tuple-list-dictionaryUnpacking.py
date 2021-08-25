# tuple and list unpacking
# We can pass in a tuple or list with the same length as the params of a function
# with a * before the list/tuple name. The * will unpack the collection and turn
# each item into individual method arguments

def sum(num1, num2, num3):
    return num1+num2+num3

# individual params
print(sum(1,4,4))  # 9

# unpack tuple into params
param_tuple = (1, 2, 3)
print(sum(*param_tuple))  # 6

# unpack list into params
param_list = [3, 4, 5]
print(sum(*param_list))  # 12

# unpack tuple into params. function definition packs it back into tuples using *args
def sum_all_values(*args): # *args combines all arguments into a tuple
    print(type(args))
    print(args)
    total= 0
    for v in args:
        total +=v
    return total

nums = (1,2,3,4,5,6,7)  # tuple
print(sum_all_values(*nums))  # 28  # *nums unpacks the tuple into arguments
nums = [1,2,3,4,5,6,7]  # list
print(sum_all_values(*nums))  # 28  # *nums unpacks the list into arguments

# TODO Dictionary unpacking
# uses ** to unpack dioctionary items into argument