# rsa_algorithm

RSA Algorithm Public Key Encryption Technique 

RSA is a type of public-key encryption method whose security is based on the algorithmic difficulty of factoring integers. It was discovered by Ron Rivest, Adi Shamir and Leonard Adleman in 1978. An RSA user generates the product of two large prime numbers and declares it as a public key along with another value of his choice. It keeps the prime factors selected. Anyone using the public key can encrypt any message.

Two sufficiently large prime numbers are chosen:

Let these numbers be p and q in our example.

n = p*q

φ (n) = (p-1) (q-1) (Totient value)

1 <e <φ (n)

d ≡ 1 mod (φ (n)). (the inverse of e with respect to mod (φ (n)) multiplication)

Encryption process:

c = m

e mod n

Password Solution:

m = c

d mod n
