def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 100
b = 200
print(gcd(a, b))
