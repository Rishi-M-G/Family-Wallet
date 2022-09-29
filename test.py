class Bank:
    def __init__(self):
        self.numberOfAcc = 0
        self.balance = None
        self.name = None
        self.accNo = None
        print("Welcome to the Bank")

    # accNo_list = []

    # ****************CREATE BANK ACCOUNT******************
    def createAccount(self):
        self.accNo = int(input("Enter the desired bank account number"))
        self.name = input("Enter the account holder's name")
        self.balance = int(input("Enter the initial amount to be deposited in the account"))
        self.numberOfAcc = self.numberOfAcc + 1
        return BankAccount(self.accNo, self.name, self.balance)

    # def showAccount(self):


class BankAccount(Bank):
    def __init__(self, accNo, name, balance):
        super().__init__()
        self.balance = balance
        self.name = name
        self.accNo = accNo
        print("***ACCOUNT CREATED***")


bacc1 = Bank()
bacc1.createAccount()
