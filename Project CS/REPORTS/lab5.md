# Topic: Web Authentication & Authorisation.

### Course: Cryptography & Security
### Author: Tincu Catalin

----

## Overview

&ensp;&ensp;&ensp; Authentication & authorization are 2 of the main security goals of IT systems and should not be used interchangibly. Simply put, during authentication the system verifies the identity of a user or service, and during authorization the system checks the access rights, optionally based on a given user role.

&ensp;&ensp;&ensp; There are multiple types of authentication based on the implementation mechanism or the data provided by the user. Some usual ones would be the following:
- Based on credentials (Username/Password);
- Multi-Factor Authentication (2FA, MFA);
- Based on digital certificates;
- Based on biometrics;
- Based on tokens.

&ensp;&ensp;&ensp; Regarding authorization, the most popular mechanisms are the following:
- Role Based Access Control (RBAC): Base on the role of a user;
- Attribute Based Access Control (ABAC): Based on a characteristic/attribute of a user.


## Objectives:
1. Take what you have at the moment from previous laboratory works and put it in a web service / serveral web services.
2. Your services should have implemented basic authentication and MFA (the authentication factors of your choice).
3. Your web app needs to simulate user authorization and the way you authorise user is also a choice that needs to be done by you.
4. As services that your application could provide, you could use the classical ciphers. Basically the user would like to get access and use the classical ciphers, but they need to authenticate and be authorized. 

   
## My Project consists of some get, post, put and delete operations on a server that will interact with users:

1. First I need to define two blocks of json data, first will have 2 users by default and second block will consist from keys for methods that will encode users passwords
```
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

```
2. Second part is to create some GET functions to visualize the keys available for each method and all the users 
```
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


@app.route('/users/keys', methods=['GET'])
def get_keys():
    return jsonify({'keys': keys})
```
3. Also, I would like to have a GET functions for each user separately based on user_id, this could be considered as user view, if the user with that id isn't created, by searching you will get an error responce
```
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = [user for user in users if user['user id'] == user_id]
    if len(user) == 0:
        abort(404)
    return jsonify({'task': user[0]})
```
4. Error Handler
```
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found, this task does not exist in datastore'}), 404)
```
5. Next item on the list is POST, basically that's how user will be added
```
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
    return jsonify({'task': user}), 201
```
6. Also, the option to change some information about a specific user need to be implemented, I 
```
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_task(user_id):
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
    return jsonify({'task': user[0]})
```
7. Last but not least is DELETE  
```
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = [user for user in users if user['user id'] == user_id]
    if len(user) == 0:
        abort(404)
    users.remove(user[0])
    return jsonify({'result': True})

```
## Output of the program:
1. I run the server first
```
* Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 730-846-179
```
2. For the tests I used Postman, first thing I did is to check global get for users and keys
```
GET http://127.0.0.1:5000/users
{
    "users": [
        {
            "access": true,
            "encoded": "QD UW AW IT EN",
            "method": "CipherPlayFair",
            "password": "LADDYBIRD",
            "user id": 1,
            "user name": "Daniel"
        },
        {
            "access": false,
            "encoded": "UUFRJDE",
            "method": "CipherVigenere",
            "password": "SUNRISE",
            "user id": 2,
            "user name": "Alex"
        }
    ]
}
GET http://127.0.0.1:5000/users/keys
 {
    "keys": [
        {
            "key": "RESPONSEDUE",
            "method": "CipherPlayFair",
            "user key": 1
        },
        {
            "key": "CASABLANCA",
            "method": "CipherVigenere",
            "user key": 2
        }
    ]
}
```
- User id: Identification
- User name: It's pretty obvious here
- Password: Users password if "Access" if True
- Encoded: Is the password encrypted
- Method: Encryption Method
- Access: stands for password view when we get user id separately, that will show below
- Key: The key used for encryption
3. User use case is a get request for a specific id, cause the "access" is false, user cannot view the password, just the encoded version
```
GET http://127.0.0.1:5000/users/2
{
    "user": {
        "access": false,
        "encoded": "UUFRJDE",
        "method": "CipherVigenere",
        "user id": 2,
        "user name": "Alex"
    }
}
```
4. Creating a new user with POST, the user id will be generated automatically and encoded version of password the same based on method selected
```
POST http://127.0.0.1:5000/users
{   
        "user name": "David",
        "password": "HAMSTER",
        "method": "CipherPlayFair",
    }
-------------------------------------------
GET http://127.0.0.1:5000/users/3
{
    "user": {
        "access": false,
        "encoded": "QH XU LO SV",
        "method": "CipherPlayFair",
        "user id": 3,
        "user name": "David"
    }
}
```
5. Next option is PUT, it was created mostly for changing something that was entered by mistake
```
PUT http://127.0.0.1:5000/users/3
{
    "access": true
}
-------------------------------------------
GET http://127.0.0.1:5000/users/3
{
    "user": {
        "access": false,
        "encoded": "QH XU LO SV",
        "method": "CipherPlayFair",
        "password": "HAMSTER",
        "user id": 3,
        "user name": "David"
    }
}
```
6. The last option is deleting a user, which  is optional
```
DELETE http://127.0.0.1:5000/users/3
{
    "result": true
}
-------------------------------------
GET http://127.0.0.1:5000/users
{
    "users": [
        {
            "access": true,
            "encoded": "QD UW AW IT EN",
            "method": "CipherPlayFair",
            "password": "LADDYBIRD",
            "user id": 1,
            "user name": "Daniel"
        },
        {
            "access": false,
            "encoded": "UUFRJDE",
            "method": "CipherVigenere",
            "password": "SUNRISE",
            "user id": 2,
            "user name": "Alex"
        }
    ]
}
```
7. Request section in the console
```
127.0.0.1 - - [15/Dec/2022 01:18:25] "GET /users/2 HTTP/1.1" 200 -
127.0.0.1 - - [15/Dec/2022 01:21:16] "POST /users HTTP/1.1" 201 --
127.0.0.1 - - [15/Dec/2022 01:24:45] "GET /users/3 HTTP/1.1" 200 -
127.0.0.1 - - [15/Dec/2022 01:33:03] "PUT /users HTTP/1.1" 200 -
127.0.0.1 - - [15/Dec/2022 01:34:59] "GET /users HTTP/1.1" 201 -
127.0.0.1 - - [15/Dec/2022 01:38:17] "DELETE /users/3 HTTP/1.1" 200 -
127.0.0.1 - - [15/Dec/2022 01:39:29] "GET /users HTTP/1.1" 200 -
```