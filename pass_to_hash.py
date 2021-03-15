import hashlib

def encrypt_string(plain_string):
    sha_signature = hashlib.sha256(plain_string.encode()).hexdigest()
    return sha_signature

