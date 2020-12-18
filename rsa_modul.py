def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


def totient(p, q):
    return (p - 1) * (q - 1)


def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None


def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x, a) is not None:
            l.append(x)
    for x in l:
        if x == modinv(x, a):
            l.remove(x)
    return l


def enc(s, e, n):
    return (pow(s, e)) % n


def dec(encr, d, n):
    return (pow(encr, d)) % n
