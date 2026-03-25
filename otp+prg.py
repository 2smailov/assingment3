import hashlib

def prg(seed, length):
    output = b""
    counter = 0
    
    while len(output) < length:
        data = seed + counter.to_bytes(4, 'big')
        output += hashlib.sha256(data).digest()
        counter += 1
    
    return output[:length]

def otp_prg_encrypt(seed, plaintext):
    plaintext_bytes = plaintext.encode()
    keystream = prg(seed, len(plaintext_bytes))
    
    ciphertext = bytes([p ^ k for p, k in zip(plaintext_bytes, keystream)])
    return ciphertext

def otp_prg_decrypt(seed, ciphertext):
    keystream = prg(seed, len(ciphertext))
    plaintext_bytes = bytes([c ^ k for c, k in zip(ciphertext, keystream)])
    return plaintext_bytes.decode()

# Example
seed = b"secret_seed"
message = "Hello World"

cipher = otp_prg_encrypt(seed, message)
print("Cipher:", cipher)

plain = otp_prg_decrypt(seed, cipher)
print("Decrypted:", plain)
