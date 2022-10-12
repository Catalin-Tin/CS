# Topic: Intro to Cryptography. Classical ciphers. Caesar cipher.

### Course: Cryptography & Security
### Author: Tincu Catalin FAF-201

----

## Overview
&ensp;&ensp;&ensp; Cryptography consists a part of the science known as Cryptology. The other part is Cryptanalysis. There are a lot of different algorithms/mechanisms used in Cryptography, but in the scope of these laboratory works the students need to get familiar with some examples of each kind.

&ensp;&ensp;&ensp; First, it is important to understand the basics so for the first task students will need to implement a classical and relatively simple cipher. This would be the Caesar cipher which uses substitution to encrypt a message. 

&ensp;&ensp;&ensp; In it's simplest form, the cipher has a key which is used to substitute the characters with the next ones, by the order number in a pre-established alphabet. Mathematically it would be expressed as follows:

$em = enc_{k}(x) = x + k (mod \; n),$

$dm = dec_{k}(x) = x + k (mod \; n),$ 

where:
- em: the encrypted message,
- dm: the decrypted message (i.e. the original one),
- x: input,
- k: key,
- n: size of the alphabet.

&ensp;&ensp;&ensp; Judging by the encryption mechanism one can conclude that this cipher is pretty easy to break. In fact, a brute force attack would have __*O(nm)*__ complexity, where __*n*__ would be the size of the alphabet and __*m*__ the size of the message. This is why there were other variations of this cipher, which are supposed to make the cryptanalysis more complex.


## Objectives:
1. Get familiar with the basics of cryptography and classical ciphers.

2. Implement 4 types of the classical ciphers:
    - Caesar cipher with one key used for substitution (as explained above),
    - Caesar cipher with one key used for substitution, and a permutation of the alphabet,
    - Vigenere cipher,
    - Playfair cipher.
    - If you want you can implement other.

3. Structure the project in methods/classes/packages as neeeded.

   
## Caesar cipher with one key used for substitution:

1. For this cipher I didn't create that much of functions or clases, just one that I will use when will get any duplicates

```
def duplicates(list):
    key = []
    for i in list:
        if i not in key:
            key.append(i)

    return key

```

2. This is the output of my program
```
--------Encryption---------
Keyword :  Best Course
Message before Ciphering :  FAF Community
Ciphered Text :  OBO SJHHQIAPY
--------Decryption----------
Keyword :  Best Course
Ciphered Text :  OBO SJHHQIAPY
Message before Ciphering :  FAF COMMUNITY
```
## Caesar cipher with one key used for substitution, and a permutation of the alphabet
1. For this cipher i used the same function from the previous cipher for the duplicates
```
def duplicates(list):
    key = []
    for i in list:
        if i not in key:
            key.append(i)

    return key

```
2. Next function is for encrypting the message after substitution with a keyword by permutation with a specific digit
```
def encrypt(key, messages):
    messages = messages.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in messages:
        if letter in alpha:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result
```
3. Next function is for decrypting the message after a succesful encryption of the inial message, actually is the same function as the one above but reversed, it was +key now is -key
```
def decrypt(key, messages):
    messages = messages.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in messages:
        if letter in alpha:  # if the letter is actually a letter
            # find the corresponding ciphertext letter in the alphabet
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

```
4. The output of the program
```
--------Encryption---------
Keyword :  Best Course
Message before Ciphering :  FAF Community
Ciphered Text :  OBO SJHHQIAPY
Ciphered Text with Permutation : RER VMKKTLDSB
--------Decryption----------
Ciphered Text without Permutation : OBO SJHHQIAPY
Keyword :  Best Course
Ciphered Text :  OBO SJHHQIAPY
Message before Ciphering :  FAF COMMUNITY
```
## Vigenere cipher
1. For this specific cipher will be much easier to adjust the text with a specific function that will allow us easier to manipulate while encrypting or decrypting 
```
def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))
```
2. Second function used in my load is for encrypting the message, since we need mod 26, it is necessary to convered the words in some integer units, for this porpuse i used ord()
```
def encryption(string, key):
    encrypt_text = []
    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26
        x += ord('A')
        encrypt_text.append(chr(x))
    return ("".join(encrypt_text))
```
3. Thrid and last function is for decrypting the message, also the same algorithm as in encryption, the only difference is -ord(key), when in the encryption was +ord(key)
```
def decryption(encrypt_text, key):
    orig_text = []
    for i in range(len(encrypt_text)):
        x = (ord(encrypt_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))
```
4. The output of the program
```
Enter the message: HELLOKYLE
Enter the keyword: ENTRY
Encrypted message: LRECMOLEV
Decrypted message: HELLOKYLE
```
## Playfair cipher
1. Function for the matrix
```
def matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]
```
2. Get the location of each character
```
def locindex(c):
    loc = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(my_matrix):
        for k, l in enumerate(j):
            if c == l:
                loc.append(i)
                loc.append(k)
                return loc
```
3. Function for Encrypting the message
```
def encrypt(): 
    msg = str(input("ENTER MSG:"))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    i = 0
    for s in range(0, len(msg) + 1, 2):
        if s < len(msg) - 1:
            if msg[s] == msg[s + 1]:
                msg = msg[:s + 1] + 'X' + msg[s + 1:]
    if len(msg) % 2 != 0:
        msg = msg[:] + 'X'
    print("CIPHER TEXT:", end=' ')
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5]), end=' ')
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        i = i + 2
```
4. Function for Decrypting the message
```
def decrypt():  
    msg = str(input("ENTER CIPHER TEXT:"))
    msg = msg.upper()
    msg = msg.replace(" ", "")
    print("PLAIN TEXT:", end=' ')
    i = 0
    while i < len(msg):
        loc = list()
        loc = locindex(msg[i])
        loc1 = list()
        loc1 = locindex(msg[i + 1])
        if loc[1] == loc1[1]:
            print("{}{}".format(my_matrix[(loc[0] - 1) % 5][loc[1]], my_matrix[(loc1[0] - 1) % 5][loc1[1]]), end=' ')
        elif loc[0] == loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1] - 1) % 5], my_matrix[loc1[0]][(loc1[1] - 1) % 5]), end=' ')
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]), end=' ')
        i = i + 2
```
5. The output of the program
```
Enter key CATALIN
ENTER MSG:PROCESSORINTEL
CIPHER TEXT: QS GI MY UM UT DC ME /n
ENTER CIPHER TEXT:QS GI MY UM UT DC ME
PLAIN TEXT: PR OC ES SO RI NT EL 
```
