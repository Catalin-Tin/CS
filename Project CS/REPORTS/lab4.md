# Topic: Hash functions and Digital Signatures.

### Course: Cryptography & Security
### Author: Catalin Tincu FAF-201

----

## Overview
&ensp;&ensp;&ensp; Hashing is a technique used to compute a new representation of an existing value, message or any piece of text. The new representation is also commonly called a digest of the initial text, and it is a one way function meaning that it should be impossible to retrieve the initial content from the digest.

&ensp;&ensp;&ensp; Such a technique has the following usages:
  * Offering confidentiality when storing passwords,
  * Checking for integrity for some downloaded files or content,
  * Creation of digital signatures, which provides integrity and non-repudiation.

&ensp;&ensp;&ensp; In order to create digital signatures, the initial message or text needs to be hashed to get the digest. After that, the digest is to be encrypted using a public key encryption cipher. Having this, the obtained digital signature can be decrypted with the public key and the hash can be compared with an additional hash computed from the received message to check the integrity of it.


## Algorithm BCrypt
Bcrypt is a password hashing function designed by Nelis Provos and David Mazières. 
Bcrypt uses strong cryptography to hash and salts password based on the Blowfish cipher. 
To make encryption stronger we can increase the “cost factor” so it can be increased as computers become faster. It is also intended to be slow, to make the brute force attacks slower and harder.

The functions in Bcrypt used –

bcrypt.gensalt() –  It is used to generate salt. Salt is a pseudorandom string that is added to the password. Since hashing always gives the same output for the same input so if someone has access to the database, hashing can be defeated. for that salt is added at end of the password before hashing. It doesn’t need any arguments and returns a pseudorandom string.

bcrypt.hashpw() – It is used to create the final hash which is stored in a database.

Arguments – We can pass Salt and Password in form of bytecode.

Return value – If hashing is successful, it returns a hash string.


## Objectives:
1. Get familiar with the hashing techniques/algorithms.
2. Use an appropriate hashing algorithms to store passwords in a local DB.
    1. You can use already implemented algortihms from libraries provided for your language.
    2. The DB choise is up to you, but it can be something simple, like an in memory one.
3. Use an asymmetric cipher to implement a digital signature process for a user message.
    1. Take the user input message.
    2. Preprocess the message, if needed.
    3. Get a digest of it via hashing.
    4. Encrypt it with the chosen cipher.
    5. Perform a digital signature check by comparing the hash of the message with the decrypted one.

   
## Hashing Passwords with BCrypt and storing the data in MySQL:
1. First step is to create a function that will hash the passwords
```
def bcrypt_algorithm(password):
    # converting password to array of bytes
    bytes = password.encode('utf-8')

    # generating the salt
    salt = bcrypt.gensalt()

    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)

    return hash
```
2. Second phase is to either create SQL database in the PYcharm or in SQL Server Management Studio, after that we will try to sign in using mysql.connector.connect by inputing the host, user, password and database that we will use. The host, user name, passwords will be covered from the security perspective
```
data = mysql.connector.connect(
    host="$$$$$$$$$$$$$",
    user="$$$$$$",
    password="$$$$$$$$$$$$",
    database="CS"
)
```
3. Third step consists of generating some passwords, that will be hashed by bcrypt_algorithm created earlier and insert the results in the created columns from database 
```
sql = "INSERT INTO password (LOGIN, PASSWORD) VALUES (%s, %s)"
val1 = ("John", f"{bcrypt_algorithm(password1)}")
val2 = ("Chris", f"{bcrypt_algorithm(password2)}")
val3 = ("Kevin", f"{bcrypt_algorithm(password3)}")
```
4. The output of the console
```
John b'$2b$12$cm6B1aJgdiXhOD.aPVyG1uz09SBzBOSBr2hCGYifGah6iW171PTPW'
record inserted.
Chris b'$2b$12$fdNxGKX5KBtUbr1NiuvuGOYWgME8h5rN.D6oLFCdg6CU9gTk20wWy'
record inserted.
Kevin b'$2b$12$Z0ij/GJLam1MJhVnMeTYbOWXNLOCEfetM2kKQBj1HzhgGteHIs5oG'
record inserted.
```
5. Last step is to open the database and check the results
![](../SCREENSHOTS/cs4lab.JPG)

## Digital Signature using Bcrypt and Elgamal
1. First step is to encrypt one of the 3 passwords hashed above using Elgamal functions from laboratory 3, where priv is the private key 
```
hashed_msg = elgamal.encrypt(priv, bcrypt_algorithm(password1))
```
2. Next step I need to create a function that will check is the string before the Elmagal encryption is the same as the string after Elgamal decryption
```
def digital_control_signature(hash_msg, encrypted_msg, public_key):
    if elgamal.decrypt(public_key, encrypted_msg) == hash_msg:
        print("True Signature")
    else:
        print("Invalid Signature")
```
3. And the last step is to call the function responsible for digital siganture in main and show the ouptput of the program
```
digital_signature.digital_control_signature(bcrypt_algorithm(password1), hashed_msg, pub)
```
```
John b'$2b$12$tO/o9itjUjXM5b9EVpZ9sednbuqpjr3T2ra4ZljchZS7nB8/toxh.'
record inserted.
Chris b'$2b$12$AWJnaI4rab3t2W4hBvONeewFcOuEX8c2v8hMjF04ofZfMfftbpSlu'
record inserted.
Kevin b'$2b$12$cJcwjuHiMEP.UpaDl8YnVuKye.Us6QDehxwpicu3JpOxuS9V3JDpS'
record inserted.
True Signature
```
