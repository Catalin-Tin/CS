import string


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


def duplicates(list):
    key = []
    for i in list:
        if i not in key:
            key.append(i)

    return key


all_alphabets = list(string.ascii_uppercase)  # stores all upper case alphabets
keyword = "Best Course"
keyword1 = keyword.upper()
message = "FAF Community"

# converts message to list
msg = []
for i in message:
    msg.append(i.upper())

# removes default elements


keyword1 = duplicates(keyword1)

# Stores the encryption list
encrypting = duplicates(keyword1 + all_alphabets)

# removes spaces from the encryption list
for i in encrypting:
    if i == ' ':
        encrypting.remove(' ')

ciphertext = ""

# maps each element of the message to the encryption list and stores it in ciphertext
for i in range(len(msg)):
    if msg[i] != ' ':
        ciphertext = ciphertext + encrypting[all_alphabets.index(msg[i])]
    else:
        ciphertext = ciphertext + ' '
print("--------Encryption---------")
print("Keyword : ", keyword)
print("Message before Ciphering : ", message)
print("Ciphered Text : ", ciphertext)
encrypted = encrypt(3, ciphertext)
print("Ciphered Text with Permutation :", encrypted)

# STARTING THE DECRYPTION PROCESS

print("--------Decryption----------")
decrypted = decrypt(3, encrypted)
print("Ciphered Text without Permutation :", decrypted)

all_alphabets = list(string.ascii_uppercase)
keyword1 = keyword.upper()
ct = []
for i in ciphertext:
    ct.append(i.upper())

# removes default elements


keyword1 = duplicates(keyword1)

# Stores the encryption list
encrypting = duplicates(keyword1 + all_alphabets)

# removes spaces from the encryption list
for i in encrypting:
    if i == ' ':
        encrypting.remove(' ')

# maps each element of the message to the encryption list and stores it in ciphertext
message = ""
for i in range(len(ct)):
    if ct[i] != ' ':
        message = message + all_alphabets[encrypting.index(ct[i])]
    else:
        message = message + ' '
print("Keyword : ", keyword)
print("Ciphered Text : ", ciphertext)
print("Message before Ciphering : ", message)

