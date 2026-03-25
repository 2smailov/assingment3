import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        g, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (g, x, y)

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception("No modular inverse")
    return x % phi

def generate_keys():
    p = 61
    q = 53
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17  
    d = mod_inverse(e, phi)

    return (e, n), (d, n)

def encrypt(public_key, plaintext):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    d, n = private_key
    return ''.join(chr(pow(char, d, n)) for char in ciphertext)

public_key, private_key = generate_keys()

message = "HELLO"
cipher = encrypt(public_key, message)
print("Cipher:", cipher)

decrypted = decrypt(private_key, cipher)
print("Decrypted:", decrypted)
