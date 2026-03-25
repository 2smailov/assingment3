import os
import random

def prg(s, length, p, g):
    res = []
    curr = s
    for _ in range(length):
        curr = pow(g, curr, p)
        res.append(curr & 0xFF)
    return bytes(res)

def main():
    
    p = 37
    g = 13
    s = random.randint(2, p-2)
    
    print(f"parameters: p={p}, g={g}")
    print(f"s: {s}")
    print()
    
    random_bytes = prg(s, 16, p, g)
    print(f"generated 16 bytes: {random_bytes.hex()}")
if __name__ == "__main__":
    main()
