# http://muhammetbaykara.com/wp-content/uploads/2017/10/kriptoloji_steganografi.pdf
# http://muhammetbaykara.com/wp-content/uploads/2017/10/Sifreleme_Bilimi_ve_Sifreleme_Teknikleri.pdf
# https://tr.wikipedia.org/wiki/RSA_(%C5%9Fifreleme_y%C3%B6netimi)
# -*- coding: utf-8 -*-

import rsa_modul as rm

p = int(input("Please enter a prime number: "))

if not rm.isPrime(p):
    print("ERROR!! p is not prime")
    exit()

q = int(input("Please enter a prime number: "))

if not rm.isPrime(p):
    print("ERROR!! q is not prime")
    exit()

n = int(p * q)
t = rm.totient(p, q)
print("Totient: {0}".format(t))

print("Choose an e from a coprime(s) array below:\n")
print(str(rm.coprimes(t)) + "\n")

e = int(input("Choose coprime number: "))
d = int(rm.modinv(e, t))

print("\ne= {0},   n= {1} \n".format(str(e), str(n)))
print("d= {0},   n= {1} \n".format(str(d), str(n)))


s = int(input("Enter a message to encrypt: "))
print("\nPlain message: " + str(s) + "\n")

enc = rm.enc(s, e, n)
print("Encrypted message: {0} \n".format(str(enc)))

dec = rm.dec(enc, d, n)
print("Decrypted message: {0} \n".format(str(dec)))
