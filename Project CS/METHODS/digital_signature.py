import elgamal


def digital_control_signature(hash_msg, encrypted_msg, public_key):
    if elgamal.decrypt(public_key, encrypted_msg) == hash_msg:
        print("True Signature")
    else:
        print("Invalid Signature")
