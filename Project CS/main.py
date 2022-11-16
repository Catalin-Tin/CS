import mysql.connector
from alg_bcrypt import bcrypt_algorithm
import elgamal
import digital_signature

data = mysql.connector.connect(
    host="$$$$$$$$$$$$$",
    user="$$$$$$",
    password="$$$$$$$$$$$$",
    database="CS"
)

password1 = "FAF-201"
password2 = "CEITI-202"
password3 = "TUM-203"

mycursor = data.cursor()

sql = "INSERT INTO password (LOGIN, PASSWORD) VALUES (%s, %s)"
val1 = ("John", f"{bcrypt_algorithm(password1)}")
val2 = ("Chris", f"{bcrypt_algorithm(password2)}")
val3 = ("Kevin", f"{bcrypt_algorithm(password3)}")

mycursor.execute(sql, val1)
mycursor.execute(sql, val2)
mycursor.execute(sql, val3)

data.commit()

print(mycursor.rowcount, "record inserted.")
keys = elgamal.generate_keys()
priv = keys['privateKey']
pub = keys['publicKey']
#message = "My name is Catalin and I am studying at FAF-201"
#cipher = elgamal.encrypt(pub, message)
#plain = elgamal.decrypt(priv, cipher)
#print("The encrypted text was: ", cipher)
#print("The text is:", plain)


hashed_msg = elgamal.encrypt(priv, bcrypt_algorithm(password1))

digital_signature.digital_control_signature(bcrypt_algorithm(password1), hashed_msg, pub)
