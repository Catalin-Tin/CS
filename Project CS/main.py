import elgamal

keys = elgamal.generate_keys()
priv = keys['privateKey']
pub = keys['publicKey']
message = "My name is Catalin and I am studying at FAF-201"
cipher = elgamal.encrypt(pub, message)
plain = elgamal.decrypt(priv, cipher)
print("The encrypted text was: ", cipher)
print("The text is:", plain)
