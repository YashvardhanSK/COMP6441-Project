import hashlib

def hash_password(password, algorithm):
    hash = hashlib.new(algorithm)
    hash.update(password.encode())
    return hash.hexdigest()