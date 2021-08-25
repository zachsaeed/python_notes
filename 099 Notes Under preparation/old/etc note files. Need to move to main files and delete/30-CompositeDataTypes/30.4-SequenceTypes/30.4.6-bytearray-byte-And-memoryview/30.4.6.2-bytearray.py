# TODO

# A bytesarray object is a sequence that is mutable and iterable.
# It returns an array of the given byte size.

a = bytearray(4)
print(a)  # bytearray(b'\x00\x00\x00\x00')
print(a[0])

a[0] = 255
print(a)
print(a[0])