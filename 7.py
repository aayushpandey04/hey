# Given string
s = "Hello World"

print("Original String:", s)

# AND operation with 127
and_result = ""
for ch in s:
    and_result += chr(ord(ch) & 127)

print("After AND with 127:", and_result)

# XOR operation with 127
xor_result = ""
for ch in s:
    xor_result += chr(ord(ch) ^ 127)

# Use repr() to safely display non-printable characters
print("After XOR with 127:", repr(xor_result))
