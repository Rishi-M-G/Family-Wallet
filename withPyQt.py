# ********** IMPORTS Starts **********
from datetime import datetime
import sys
import csv
import pandas as pd


# ********** IMPORTS Ends **********

# ********** CLASSES Starts **********
# ********** BANK CLASS Starts **********
class Bank:
    accNo = None
    balance = None
    name = None
    acc_List = []
    accNo_List = []
    transaction_list = []
    temp = None
    temp1 = None

    # Constructor Method
    def __init__(self):
        pass

    # Loading Lists from CSV File
    def Bank_loadList(self):
        dframe = pd.read_csv("C:\\Users\\Dell\\Desktop\\WalletTest.csv")
        from_df = pd.DataFrame(dframe)
        self.acc_List = from_df['acc_List'].values.tolist()
        self.accNo_List = from_df['accNo_List'].values.tolist()
        self.transaction_list = from_df['transaction_list'].values.tolist()

    # Creating a Bank Account
    def createAccount(self):
        print(self.acc_List)
        self.accNo = int(input("Enter the desired bank account number"))
        self.name = input("Enter the account holder's name")
        self.balance = int(input("Enter the initial amount to be deposited in the account"))
        print("***ACCOUNT CREATED***")
        self.acc_List.append([self.accNo, self.name, self.balance])
        self.accNo_List.append(self.accNo)

    # Show Bank Account Details
    def showAccount(self, accno):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
            print("Account Number: ", self.acc_List[self.accNo_List.index(accno)][0])
            print("Account Holder Name:", self.acc_List[self.accNo_List.index(accno)][1])
            print("Account Balance:", self.acc_List[self.accNo_List.index(accno)][2])

    # Delete an Account from the Bank
    def deleteAccount(self, accno):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
            self.acc_List.remove(self.acc_List[self.accNo_List.index(accno)])
            print("YOUR ACCOUNT HAS BEEN CLOSED")

    # Modify Account Information (Only Name can be modified)
    def modifyAccount(self, accno):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
            print("*****MODIFY ACCOUNT DETAILS*****")
            print("NOTE : YOU CANNOT MODIFY ACCOUNT NUMBER")
            self.acc_List[self.accNo_List.index(accno)][1] = input("Enter Account Holder's Name")
            print("ACCOUNT INFO MODIFIED")

    # Load Lists back to CSV File
    def Bank_storeList(self):
        data = {'acc_List': self.acc_List,
                'accNo_List': self.accNo_List,
                'transaction_List': self.transaction_list}
        to_df = pd.DataFrame(data, columns=['acc_List', 'accNo_List', 'transaction_list'])
        to_df.to_csv(r'C:\Users\Dell\Desktop\WalletTest.csv', index=False, header=True)


# ********** BANK CLASS Ends **********
# ********** WALLET CLASS Starts **********
class Wallet(Bank):
    wallet_acc_list = []
    acc_no_wallet = None
    wallet_balance = None

    def __init__(self):
        super().__init__()
        pass

    def Wallet_LoadList(self):
        dframe = pd.read_csv("C:\\Users\\Dell\\Desktop\\WalletTest.csv")
        from_df = pd.DataFrame(dframe)
        self.wallet_acc_list = from_df['wallet_acc_list'].values.tolist()

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

    def removeAccount(self, accno):
        if accno in self.accNo_List:
            self.wallet_acc_list.remove(
                [self.acc_List[self.accNo_List.index(accno)][0], self.acc_List[self.accNo_List.index(accno)][1],
                 self.acc_List[self.accNo_List.index(accno)][2]])
            print("BANK ACCOUNT {0} HAS BEEN REMOVED FROM THE WALLET ".format(accno))

    def addMoneyToWallet(self, accno, amount):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
        if self.acc_List[self.accNo_List.index(accno)][2] < amount:
            print("There is not enough balance in this account")
        else:
            self.wallet_balance = amount
            self.acc_List[self.accNo_List.index(accno)][2] = self.acc_List[self.accNo_List.index(accno)][2] - amount
            print("CURRENT WALLET BALANCE: ", self.wallet_balance)

    def withdrawMoneyFromWallet(self, accno, amount):
        if accno in self.accNo_List:
            print(self.accNo_List.index(accno))
        if self.wallet_balance < amount:
            print("There is not enough balance in wallet")
        else:
            self.acc_List[self.accNo_List.index(accno)][2] = self.acc_List[self.accNo_List.index(accno)][2] + amount
            self.wallet_balance = self.wallet_balance - amount
            print("CURRENT WALLET BALANCE: ", self.wallet_balance)

    def Wallet_storeList(self):
        data = {'wallet_acc_list': self.wallet_acc_list}
        to_df = pd.DataFrame(data, columns=['wallet_acc_list'])
        to_df.to_csv(r'C:\Users\Dell\Desktop\WalletTest.csv', index=False, header=True)



# ********** WALLET CLASS Ends **********
# ********** CLASSES Ends **********


# ********** MAIN CLASS **********
b = Bank()
b.Bank_loadList()
