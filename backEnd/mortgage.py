'''
    This file is for the main stuff about mortgage (Init customers, calculate all the related stuffs, prediction...)
    Using: Basic calculation, and machine learning
'''

import datetime
from cryptography.fernet import Fernet

class Client:
    '''
        Client class
        Attributes:
            fName: first name
            mName: middle name
            lName: last name
            dob: date of birth (mm/dd/yyyy)
            ssn: social security number (need encrypt - hide)
            address: {street#}{street name}{suite/room}{zip}
            incomes: dictionary of income sources (Income class)
            assets: dictionary of assets (Asset class)
            liabilities: dictionary of liabities (debt,...) (Liability class)
    '''

    def __init__(self, fName, mName, lName, dob, ssn, cScore, address, incomes, assets, liabilities):
        self.make_key()
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.dob = dob
        self.ssn = self.encrypt_ssn(ssn)      #Never save ssn as itself in text
        self.cScore = cScore
        self.address = address
        self.incomes = incomes
        self.assets = assets
        self.liabilities = liabilities

    def make_key(self):
        '''
        Generates key
        '''
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

    def get_key(self):
        '''
        Returns: key for encryption
        '''
        return open("secret.key", "rb").read()

    def encrypt_ssn(self, ssn):
        '''
        Encrypts the ssn using the key generated
        Args:
            ssn: ssn entered by user
        Returns: encrypted ssn
        '''
        key = self.get_key()
        encoded_ssn = ssn.encode()
        f = Fernet(key)
        encrypted_ssn = f.encrypt(encoded_ssn)
        return encrypted_ssn

    def getSSN(self, encrypted):
        '''
            Get last 4 digits of ssn
            Attributes:
                encrypted: encrypted ssn taken from server
        '''
        key = self.get_key()
        f = Fernet(key)
        last_four = f.decrypt(encrypted)
        return last_four

    def getBalance(self, income, assets, liabilities):
        '''
            Get balance by compute from income + assets - liabilities
        '''
        return (self.getDictionaryTotal(income) + self.getDictionaryTotal(assets) - self.getDictionaryTotal(liabilities))

    def getDictionaryTotal(self, dict):
        return sum(dict.values())

    def getTotalIncome(self, income):
        '''
            Get income
            W-2 + 1099*0.8 + rentalProp * 0.75
        '''
        return income.get('W-2') + income.get('1099') * 0.8 + income.get('rentalProp') * 0.75



    
