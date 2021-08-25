import sys
# A simple comparison of size (in Bytes) of lit comprehension vs generator expressions

list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")  # List Comprehension: 4516 bytes
print(f"Generator Expression: {gen_exp} bytes")  # Generator Expression: 64 bytes