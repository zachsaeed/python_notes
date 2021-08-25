# The walrus operator (:=) assigns values to variables as part of a
# larger expression.
a = "Hello. How are you?"
if (n := len(a)) > 10:
    print(f"String is too long ({n} elements, expected <= 10)")

# It essentially replaces the code:
n = len(a)
if n > 10:
    print(f"String is too long ({n} elements, expected <= 10)")

# It is useful when we need a value twice. Once to test and second to process it.
# The operator is also useful with while-loops that compute a value to
# test loop termination and then need that same value again in the body of
# the loop:

# Loop over fixed length blocks
# while ( block := f.read(256) ) != '':
#   process(block)

# Note:
# b := a+1 and
# b := (a+1) are the same

a = 11

b = 2
print(b := a + 1)  # 12
print(b)  # 12

b = 2
print(b := (a + 1))  # 12
print(b)  # 12

b = 2
print((b := a) + 1)  # 12
print(b)  # 11
