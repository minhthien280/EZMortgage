CLASSES:
    mortgage.py:
        Client: getter, setter with authorization
            fName, mName, lName, SSN(encrypted), clientID, dob, cScore, address, incomes, assets, liabilities
    security.py:
        getPublicKey(authorization)
        getPrivateKey(authorization)
        encrypt(raw, public_key)
        encrypt_file(path, destination_filename, public_key)
        decrypt(encrypted, private_key)
        decrypt_file(path, destination_filename, private_key)

ABSTRACT FUNCTION:
mortgage.py :
    - Client class:
        -- getClient()
