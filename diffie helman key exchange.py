
def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def main():
    P = 29
    G = 4
    a = 15

    x = power(G, a, P)


    b = 25
    y = power(G, b, P)

    keya = power(y, a, P)  
    keyb = power(x, b, P) 

if __name__ == "__main__":
    main()
