# class dad
class Dad:
    def __init__(self):
        print("This is Dad Class")


class Bank:
    def __init__(self):
        self.accNo = None
        self.name = None
        self.balance = None
        print("Welcome to the Bank")

    # ****************CREATE BANK ACCOUNT******************
    def createAccount(self):
        self.accNo = int(input("Enter Account Number"))
        self.name = input("Enter Account Holder Name")
        self.balance = int(input("Enter the amount for initial deposit in your account"))

        print("***ACCOUNT CREATED***")


class Wallet:
    def __init__(self):
        print("Welcome to the Family Wallet")


Bank().createAccount()
