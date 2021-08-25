# *args
# special operator we can pass to functions
# gathers remaining arguments as tuple
# you can call it whatever you want
# if we put *args as a parameter to a function, it will collect any number of
# additional / extra arguments that have been passed-in, into a single
# parameter called args


def sum_all_nums(num1, num2, num3):
    return num1 + num2 + num3


print(sum_all_nums(1, 2, 3))  # 6

# we are limited to three arguments. What i we have 10 or 20 arguments? we
# use *args as parameter. It can accept any number of arguments and treats them
# as a tuple within the function body


def sum_all_nums2(*nums):
    # nums will be treated as a tuple here
    print(type(nums))  # <class 'tuple'>
    print(nums)
    total = 0
    for num in nums:
        total += num
    return total


print(sum_all_nums2(1, 2, 3))
# <class 'tuple'>
# (1, 2, 3)
# 6

print(sum_all_nums2(1, 2, 3, 20, 1, 5))
# <class 'tuple'>
# (1, 2, 3, 20, 1, 5)
# 32

# Note: we can mix *arg with individual params but args has to be in the end
# otherwise it wont be able to differentiate b/w params and arg tuple

def func(arg1, arg2, *args):
    print(arg1, arg2, args)
