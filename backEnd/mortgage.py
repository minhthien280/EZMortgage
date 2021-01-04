'''
    This file is for the main stuff about mortgage (Init customers, calculate all the related stuffs, prediction...)
    Using: Basic calculation, and machine learning
'''
import datetime
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
            liabilities: diction of liabities (debt,...) (Liability class)
    '''
    def __init__(self):
        self.fName = ""
        self.mName = ""
        self.lName = ""
        self.dob = ""
        self.ssn = ""           #Never save ssn as itself in text
        self.cScore
        self.address = ""
        self.incomes
        self.assets
        self.liabilities

    def getSSN(privateKey, encrypted):
        '''
            Get last 4 digits of ssn
            Attributes:
                privateKey: key to decrypt the ssn
                encrypted: encrypted ssn taken from server
        '''

    def getBalance(self):
        '''
            Get balance by compute from income + assets - liabilities
        '''

    def getTotalIncome(self):
        '''
            Get income
            W-2 + 1099*0.8 + rentalProp * 0.75
        '''

    
