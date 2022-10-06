# *********** BANK CLASS ********
class Bank:
    accNo = None
    balance = None
    name = None
    acc_List = [[1001, 'Rishi', 5000], [1002, 'Mehana', 10000]]
    accNo_List = [1001, 1002]
    temp = None
    temp1 = None

    def __init__(self):
        pass

    def createAccount(self):
        print(self.acc_List)
        self.accNo = int(input("Enter the desired bank account number"))
        self.name = input("Enter the account holder's name")
        self.balance = int(input("Enter the initial amount to be deposited in the account"))
        print("***ACCOUNT CREATED***")
        self.acc_List.append([self.accNo, self.name, self.balance])
        self.accNo_List.append(self.accNo)

    def showAccount(self, accno):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
            print("Account Number: ", self.acc_List[self.accNo_List.index(accno)][0])
            print("Account Holder Name:", self.acc_List[self.accNo_List.index(accno)][1])
            print("Account Balance:", self.acc_List[self.accNo_List.index(accno)][2])

    def deleteAccount(self, accno):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
            self.acc_List.remove(self.acc_List[self.accNo_List.index(accno)])
            print("YOUR ACCOUNT HAS BEEN CLOSED")

    def modifyAccount(self, accno):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
            print("*****MODIFY ACCOUNT DETAILS*****")
            print("NOTE : YOU CANNOT MODIFY ACCOUNT NUMBER")
            self.acc_List[self.accNo_List.index(accno)][1] = input("Enter Account Holder's Name")
            print("ACCOUNT INFO MODIFIED")


# ******** WALLET CLASS ************
class Wallet(Bank):
    wallet_acc_list = []
    acc_no_wallet = None
    wallet_balance = None

    def __init__(self):
        super().__init__()
        pass

    def addAccount(self, accno):
        if len(self.wallet_acc_list) == 2:
            print("Cannot add more than two accounts")
        else:
            print("Account Number: ", self.acc_List[self.accNo_List.index(accno)][0])
            print("Account Holder's Name: ", self.acc_List[self.accNo_List.index(accno)][1])
            print("Account Balance: ", self.acc_List[self.accNo_List.index(accno)][2])
            print("THIS BANK ACCOUNT HAS BEEN ADDED TO THE WALLET")
            self.wallet_acc_list.append(
                [self.acc_List[self.accNo_List.index(accno)][0], self.acc_List[self.accNo_List.index(accno)][1],
                 self.acc_List[self.accNo_List.index(accno)][2]])

    def addMoneyToWallet(self, accno, amount):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
        if self.acc_List[self.accNo_List.index(accno)][2] < amount:
            print("There is not enough balance in this account")
        else:
            self.wallet_balance = self.acc_List[self.accNo_List.index(accno)][2] - amount
            self.acc_List[self.accNo_List.index(accno)][2] = self.acc_List[self.accNo_List.index(accno)][2] - amount
            print("CURRENT WALLET BALANCE: ", self.wallet_balance)


# ************* MAIN WINDOW *************

# Creating Bank Accounts List
# list1 = []

# CreateAccount() Method Call
# Bank().createAccount()
# list1.append(Bank().createAccount())

# Dummy Values for testing
# list1.append([1004, 'Rishi', 1000])
# list1.append([1005, 'Mehana', 10000])

# print(list1[0])
# print(list1[1])
# print("Account Number:{0}   Name:{1}   Balance:{2}".format(list1[0][0], list1[0][1], list1[0][2]))

# ShowAccount() method call
# temp1 = int(input("Enter Account Number"))
# Bank().showAccount(temp1)

# DeleteAccount() Method Call
# temp1 = int(input("Enter Account Number"))
# Bank().deleteAccount(temp1)

# list1 = Bank().deleteAccount(list1)
# print(list1)

# modifyAccount() Method Call
# temp1 = int(input("Enter Account Number"))
# Bank().modifyAccount(temp1)

# list1 = Bank().modifyAccount(list1)
# print(list1)
b = Bank()
w = Wallet()

temp1 = int(input("Enter Account Number"))
w.addAccount(temp1)
print(Wallet.wallet_acc_list)

temp2 = int(input("Enter Account Number"))
amt = int(input("Enter Amount"))
w.addMoneyToWallet(temp2,amt)
print(w.wallet_balance)
