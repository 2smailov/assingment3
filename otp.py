import random

def generate_key(plaintext_length):
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(plaintext_length))
    return key

def encrypt(plaintext, key):
    ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))
    return ciphertext


if __name__ == "__main__":
    plaintext = "FKPAPKPNNF"
    key = generate_key(len(plaintext))
    
    ciphertext = encrypt(plaintext, key)
    print(ciphertext)
