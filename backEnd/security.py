'''
    This one to secure the infomation for everything,
    secure the data: encrypt data from client-server and decrypt data from server-client
    Assymmetric encryption: RSA key gen, Use SHA-3 to hash, PKCS#1 to sign
    Maybe communicate with database here

    cryptography library example: https://nitratine.net/blog/post/asymmetric-encryption-and-decryption-in-python/
    using private_key.pem for decryption
    using public_key.pem for encryption
'''
import cryptography
import os
from cryptography.hazmat.primitives import serialization,hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding


with open('private_key.pem','rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file=read(),
        password=None,
        backend=default_backend()
    )

with open('public_key.pem','rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file=read(),
        backend=default_backend()
    )

def encrypt(raw, public_key):
    encrypted = public_key.encrypt(
        raw,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def encrypt_file(path='', destination_filename = 'encrypted.txt', public_key):
    if path=='' or (not os.path.isfile(path)):
        print('File not found')
        return False

    with (path,'rb') as f:
        raw = f.read()

    with ('./' + destination_filename, 'wb') as f:
        f.write(encrypt(raw,public_key))
        print("encrypt successfully")
        return True

def decrypt(encrypted, private_key):
    raw = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return raw

def decrypt_file(path='', destination_filename = 'raw.txt', private_key):
    if path=='' or (not os.path.isfile(path)):
        print('File not found')
        return False

    with (path,'rb') as f:
        encrypted = f.read()

    with ('./' + destination_filename, 'wb') as f:
        f.write(decrypt(encrypted, private_key))
        print("Decryption successfully")
        return True
