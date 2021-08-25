# We generally use the 'else' with 'if' conditions but python also allows us to use
# the else condition with for loops.

# The else clause executes after the loop completes normally. This means that the
# loop did not encounter a break statement
# and is NOT executed when the loop is terminated by a break statement.

# else is always executed at the end of the loop as it ends naturally
for i in range(1, 4):
    print(i)
else:  # Executed because no break in for
    print("No Break")
print('Loop ended naturally')
# 1
# 2
# 3
# No Break
# Loop ended naturally

# else block is NOT executed in below :
for i in range(1, 4):
    print(i)
    break
else:  # Not executed as there is a break
    print("No Break")
print('for Loop terminated by break')
# 1
# for Loop terminated by break

# Same with while loops
count = 0
while (count < 1):
    count = count+1
    print(count)
    break
else:
    print("No Break")
print('while loop terminated by break')
# 1
# while loop terminated by break