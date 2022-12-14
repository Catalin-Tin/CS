import mysql.connector
from METHODS, alg_bcrypt import bcrypt_algorithm
from METHODS import elgamal
from METHODS import digital_signature
from METHODS import CipherPlayFair
from METHODS import CipherSub
from METHODS import CipherSubandPer
from METHODS import CipherVigenere
from METHODS import DesBlockCipher
from METHODS import Rc4StreamCipher
import Scripts as Scripts
from flask import Flask  # General library used for server
from flask import jsonify  # Used for General Get
from flask import abort  # Used for Specific Get
from flask import make_response  # Used for Error Handler
from flask import request  # Used for Post operations


print("------------------------LAB 5--------------------------")
app = Flask(__name__)

keys = [
    {
        'user key': 1,
        'key': u'RESPONSEDUE',
        'method': u'CipherPlayFair'
    },
    {
        'user key': 2,
        'key': u'CASABLANCA',
        'method': u'CipherVigenere'
    }

]

users = [
    {
        'user id': 1,
        'user name': 'Daniel',
        'encoded': CipherPlayFair.encrypt('password'),
        'password': u'LADDYBIRD',
        'method': u'CipherPlayFair',
        'access': True
    },
    {
        'user id': 2,
        'user name': 'Alex',
        'encoded': CipherVigenere.encryption('password', CipherVigenere.generateKey('password', CipherVigenere.keyword)),
        'password': u'SUNRISE',
        'method': u'CipherVigenere',
        'access': False
    }
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@app.route('/users/keys', methods=['GET'])
def get_keys():
    return jsonify({'keys': keys})


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['user id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found, this task does not exist in datastore'}), 404)


@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or not 'user name' in request.json:
        abort(400)
    user = {
        'user id': users[-1]['user id'] + 1,
        'user name': request.json['user name'],
        'encoded': request.json.get('encoded', ""),
        'password': request.json['password'],
        'method': request.json['method'],
        'access': False
    }
    users.append(user)
    return jsonify({'user': user}), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = [user for user in users if user['user id'] == user_id]
    if len(user) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'user name' in request.json and type(request.json['user name']) != Scripts.unicode:
        abort(400)
    if 'encoded' in request.json and type(request.json['encoded']) is not Scripts.unicode:
        abort(400)
    if 'password' in request.json and type(request.json['password']) != Scripts.unicode:
        abort(400)
    if 'method' in request.json and type(request.json['method']) != Scripts.unicode:
        abort(400)
    if 'access' in request.json and type(request.json['access']) is not bool:
        abort(400)
    user[0]['title'] = request.json.get('title', user[0]['title'])
    user[0]['encoded'] = request.json.get('encoded', user[0]['encoded'])
    user[0]['password'] = request.json.get('password', user[0]['password'])
    user[0]['method'] = request.json.get('method', user[0]['method'])
    user[0]['access'] = request.json.get('access', user[0]['access'])
    return jsonify({'user': user[0]})


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['user id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)

print("------------------------LAB 4--------------------------")
#data = mysql.connector.connect(
    #host="$$$$$$$$$$$$$",
    #user="$$$$$$",
    #password="$$$$$$$$$$$$",
    #database="CS"
#)

#password1 = "FAF-201"
#password2 = "CEITI-202"
#password3 = "TUM-203"

#mycursor = data.cursor()

#sql = "INSERT INTO password (LOGIN, PASSWORD) VALUES (%s, %s)"
#val1 = ("John", f"{bcrypt_algorithm(password1)}")
#val2 = ("Chris", f"{bcrypt_algorithm(password2)}")
#val3 = ("Kevin", f"{bcrypt_algorithm(password3)}")

#mycursor.execute(sql, val1)
#mycursor.execute(sql, val2)
#mycursor.execute(sql, val3)

#data.commit()

#print(mycursor.rowcount, "record inserted.")
#keys = elgamal.generate_keys()
#priv = keys['privateKey']
#pub = keys['publicKey']

#hashed_msg = elgamal.encrypt(priv, bcrypt_algorithm(password1))
#digital_signature.digital_control_signature(bcrypt_algorithm(password1), hashed_msg, pub)

print("------------------------LAB 3--------------------------")
#message = "My name is Catalin and I am studying at FAF-201"
#cipher = elgamal.encrypt(pub, message)
#plain = elgamal.decrypt(priv, cipher)
#print("The encrypted text was: ", cipher)
#print("The text is:", plain)

print("------------------------LAB 2--------------------------")
#DesBlockCipher.encryption()
#print("---------------------------------------------------------")
#DesBlockCipher.decryption()
#print("---------------------------------------------------------")
#Rc4StreamCipher.encryption()
#print("---------------------------------------------------------")
#Rc4StreamCipher.decryption()

print("------------------------LAB 1--------------------------")
#CipherPlayFair.encrypt()
#print("/n")
#CipherPlayFair.decrypt()
#print("---------------------------------------------------------")
#message = ""
#for i in range(len(CipherSub.ct)):
    #if CipherSub.ct[i] != ' ':
        #message = message + CipherSub.all_alphabets[CipherSub.encrypting.index(CipherSub.ct[i])]
    #else:
        #message = message + ' '
#print("--------Decryption----------")
#print("Keyword : ", CipherSub.keyword)
#print("Ciphered Text : ", CipherSub.ciphertext)
#print("Message before Ciphering : ", message)
#print("---------------------------------------------------------")
#message = ""
#for i in range(len(CipherSubandPer.ct)):
    #if CipherSubandPer.ct[i] != ' ':
        #message = message + CipherSubandPer.all_alphabets[CipherSubandPer.encrypting.index(CipherSubandPer.ct[i])]
    #else:
        #message = message + ' '
#print("Keyword : ", CipherSubandPer.keyword)
#print("Ciphered Text : ", CipherSubandPer.ciphertext)
#print("Message before Ciphering : ", message)
#print("---------------------------------------------------------")
#string = input("Enter the message: ")
#keyword = input("Enter the keyword: ")
#key = CipherVigenere.generateKey(string, keyword)
#encrypt_text = CipherVigenere.encryption(string, key)
#print("Encrypted message:", encrypt_text)
#print("Decrypted message:", CipherVigenere.decryption(encrypt_text, key))
