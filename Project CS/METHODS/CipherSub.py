import string

# stores all upper case alphabets
all_alphabets = list(string.ascii_uppercase)

keyword = "Best Course"
keyword1 = keyword.upper()

message = "FAF Community"

# converts message to list
msg = []
for i in message:
    msg.append(i.upper())


# removes default elements


def duplicates(list):
    key = []
    for i in list:
        if i not in key:
            key.append(i)

    return key


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

# STARTING THE DECRYPTION PROCESS
all_alphabets = list(string.ascii_uppercase)
keyword1 = keyword.upper()
ct = []
for i in ciphertext:
    ct.append(i.upper())


keyword1 = duplicates(keyword1)

# Stores the encryption list
encrypting = duplicates(keyword1 + all_alphabets)

# removes spaces from the encryption list
for i in encrypting:
    if i == ' ':
        encrypting.remove(' ')