# Topic: Asymmetric Ciphers.

### Course: Cryptography & Security
### Author: Tincu Catalin FAF-201

----

## Overview
&ensp;&ensp;&ensp; Asymmetric Cryptography (a.k.a. Public-Key Cryptography)deals with the encryption of plain text when having 2 keys, one being public and the other one private. The keys form a pair and despite being different they are related.

&ensp;&ensp;&ensp; As the name implies, the public key is available to the public but the private one is available only to the authenticated recipients. 

&ensp;&ensp;&ensp; A popular use case of the asymmetric encryption is in SSL/TLS certificates along side symmetric encryption mechanisms. It is necessary to use both types of encryption because asymmetric ciphers are computationally expensive, so these are usually used for the communication initiation and key exchange, or sometimes called handshake. The messages after that are encrypted with symmetric ciphers.


## Example took is ElGamal
ElGamal encryption is a public-key cryptosystem. It uses asymmetric key encryption for communicating between two parties and encrypting the message.

This cryptosystem is based on the difficulty of finding discrete logarithm in a cyclic group that is even if we know ga and gk, it is extremely difficult to compute gak.
    



## Objectives:
1. Get familiar with the asymmetric cryptography mechanisms.

2. Implement an example of an asymmetric cipher.

3. As in the previous task, please use a client class or test classes to showcase the execution of your programs.

   
## Code Overview
I have 2 files, first one elgamal.py is dedicated for functions needed for elmagal itself, such as generate_keys, encrypt, decrypt, find_primitive_root, find_prime and so on. 

Second file named main.py is for inputting the data and executing the elmagal encryption and decryption.

## ElGamal.py

1. First thing to do is to create two object-oriented classes, one for public key and second for private key
```
class PrivateKey(object):
    def __init__(self, p=None, g=None, x=None, iNumBits=0):
        self.p = p
        self.g = g
        self.x = x
        self.iNumBits = iNumBits


class PublicKey(object):
    def __init__(self, p=None, g=None, h=None, iNumBits=0):
        self.p = p
        self.g = g
        self.h = h
        self.iNumBits = iNumBits
```
2. Also, I need a function of The Greatest Common Denominator of a and b, I assume that a > b
```
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    # a is returned if b == 0
    return a
```
3. I need to compute base^exp and modulus
```
def modexp(base, exp, modulus):
    return pow(base, exp, modulus)
```
4. Function solstra is nothing but a control point, that checks is the number is prime or composite, based on an algorithm called solovay-strassen primality test
```
def solstra(num, iConfidence):
    # ensure confidence of t
    for i in range(iConfidence):
        # choose random a between 1 and n-2
        a = random.randint(1, num - 1)

        # if a is not relatively prime to n, n is composite
        if gcd(a, num) > 1:
            return False

        # declares n prime if jacobi(a, n) is congruent to a^((n-1)/2) mod n
        if not jacobi(a, num) % num == modexp(a, (num - 1) // 2, num):
            return False

    # if there have been t iterations without failure, num is believed to be prime
    return True
```
5. In the function descried above we have such a function called jacobi, well this is a symbol used in solstra implemetation, symbol is described in theory as (p/n) where p is a prime number, but n is any integer number. Here it is how jacobi symbol function works:
```
def jacobi(a, n):
    if a == 0:
        if n == 1:
            return 1
        else:
            return 0
    # property 1 of the jacobi symbol
    elif a == -1:
        if n % 2 == 0:
            return 1
        else:
            return -1
    # if a == 1, jacobi symbol is equal to 1
    elif a == 1:
        return 1
    # property 4 of the jacobi symbol
    elif a == 2:
        if n % 8 == 1 or n % 8 == 7:
            return 1
        elif n % 8 == 3 or n % 8 == 5:
            return -1
    # property of the jacobi symbol:
    # if a = b mod n, jacobi(a, n) = jacobi( b, n )
    elif a >= n:
        return jacobi(a % n, n)
    elif a % 2 == 0:
        return jacobi(2, n) * jacobi(a // 2, n)
    # law of quadratic reciprocity
    # if a is odd and a is coprime to n
    else:
        if a % 4 == 3 and n % 4 == 3:
            return -1 * jacobi(n, a)
        else:
            return jacobi(n, a)
```
6. Next function finds a primitive for prime
```
def find_primitive_root(p):
    if p == 2:
        return 1
    # the prime divisors of p-1 are 2 and (p-1)/2 because
    # p = 2x + 1 where x is a prime
    p1 = 2
    p2 = (p - 1) // p1

    # test random g's until one is found that is a primitive root mod p
    while (1):
        g = random.randint(2, p - 1)
        # g is a primitive root if for all prime factors of p-1, p[i]
        # g^((p-1)/p[i]) (mod p) is not congruent to 1
        if not (modexp(g, (p - 1) // p1, p) == 1):
            if not modexp(g, (p - 1) // p2, p) == 1:
                return g
```
7. Function called find_prime uses the solstra described above for finding n bit prime
```
def find_prime(iNumBits, iConfidence):
    # keep testing until one is found
    while 1:
        # generate potential prime randomly
        p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))
        # make sure it is odd
        while p % 2 == 0:
            p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))

        # keep doing this if the solovay-strassen test fails
        while not solstra(p, iConfidence):
            p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))
            while p % 2 == 0:
                p = random.randint(2 ** (iNumBits - 2), 2 ** (iNumBits - 1))

        # if p is prime compute p = 2*p + 1
        # if p is prime, we have succeeded; else, start over
        p = p * 2 + 1
        if solstra(p, iConfidence):
            return p
```
8. Before I get to the key generator function, encrypt and decrypt, I need two functions, one that will encode bytes to integer mod p that will be used in encryption algorithm and second function that will decode integers to the original message bytes for decryption algorithm. 
   
   The function encode and decode are big enough, and I decided to not add them here, if it's necessary the functions are described in elgamal.py. Therefore, I am moving to the next function generate_keys described bellow, which generates public key K1 (p, g, h) and private key K2 (p, g, x)
```
def generate_keys(iNumBits=256, iConfidence=32):
    # p is the prime
    # g is the primitve root
    # x is random in (0, p-1) inclusive
    # h = g ^ x mod p
    p = find_prime(iNumBits, iConfidence)
    g = find_primitive_root(p)
    g = modexp(g, 2, p)
    x = random.randint(1, (p - 1) // 2)
    h = modexp(g, x, p)

    publicKey = PublicKey(p, g, h, iNumBits)
    privateKey = PrivateKey(p, g, x, iNumBits)

    return {'privateKey': privateKey, 'publicKey': publicKey}

```
9. Encrypt function encrypts a string sPlaintext using the public key k
```
def encrypt(key, sPlaintext):
    z = encode(sPlaintext, key.iNumBits)

    # cipher_pairs list will hold pairs (c, d) corresponding to each integer in z
    cipher_pairs = []
    # i is an integer in z
    for i in z:
        # pick random y from (0, p-1) inclusive
        y = random.randint(0, key.p)
        # c = g^y mod p
        c = modexp(key.g, y, key.p)
        # d = ih^y mod p
        d = (i * modexp(key.h, y, key.p)) % key.p
        # add the pair to the cipher pairs list
        cipher_pairs.append([c, d])

    encryptedStr = ""
    for pair in cipher_pairs:
        encryptedStr += str(pair[0]) + ' ' + str(pair[1]) + ' '

    return encryptedStr
```
10. The last one, decryption function performs decryption on the cipher pairs found in Cipher using private key K2 and writes the decrypted values to file Plaintext
```
def decrypt(key, cipher):
    # decrpyts each pair and adds the decrypted integer to list of plaintext integers
    plaintext = []

    cipherArray = cipher.split()
    if not len(cipherArray) % 2 == 0:
        return "Malformed Cipher Text"
    for i in range(0, len(cipherArray), 2):
        # c = first number in pair
        c = int(cipherArray[i])
        # d = second number in pair
        d = int(cipherArray[i + 1])

        # s = c^x mod p
        s = modexp(c, key.x, key.p)
        # plaintext integer = ds^-1 mod p
        plain = (d * modexp(s, key.p - 2, key.p)) % key.p
        # add plain to list of plaintext integers
        plaintext.append(plain)

    decryptedText = decode(plaintext, key.iNumBits)

    # remove trailing null bytes
    decryptedText = "".join([ch for ch in decryptedText if ch != '\x00'])

    return decryptedText
```
## Main.py
1. Importing the elgamal functions and declaring the message
```
import elgamal

keys = elgamal.generate_keys()
priv = keys['privateKey']
pub = keys['publicKey']
message = "My name is Catalin and I am studying at FAF-201"
cipher = elgamal.encrypt(pub, message)
plain = elgamal.decrypt(priv, cipher)
print("The encrypted text was: ", cipher)
print("The text is:", plain)
```
2. Output of the algorithm
```
The encrypted text was:  7285529338370717230538528304815268564962986480659216870755882262561226118373 1413215030268924418814701326568982874503743257364512190697217507388992784681 67586254465906521995885912530610637074965521515741957433091313870551324051399 42446827458653998043031639616795446295689158333050250826062453652170535501153 9269084394826640897908970535852476850529885645051857516252871529667432335212 43673560706720065544422229817741183550960051544489512871763972485958956054436 
The text is: My name is Catalin and I am studying at FAF-201
```






