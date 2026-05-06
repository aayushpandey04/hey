
import math

# Modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d

# Key generation
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)

# Find e
e = 2
while math.gcd(e, phi) != 1:
    e += 1

# Find d
d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

# 🔹 Take message from user
message = int(input("Enter message (number): "))

# Encrypt
encrypted = pow(message, e, n)
print("Encrypted:", encrypted)

# Decrypt
decrypted = pow(encrypted, d, n)
print("Decrypted:", decrypted)
