# ********** IMPORTS Starts **********
from datetime import datetime
import sys
import csv
import pandas as pd
import openpyxl


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
        dframe = pd.read_excel(r'C:\Users\Dell\Desktop\BankTest.xlsx', sheet_name='BankClass')
        from_df = pd.DataFrame(dframe)
        self.acc_List = from_df.values.tolist()
        for i in self.acc_List:
            self.accNo_List.append(i[0])

    # Creating a Bank Account
    def createAccount(self,role):
        if (role == 'Father') or (role == 'Mother'):
            self.accNo = int(input("Enter the desired bank account number"))
            self.name = input("Enter the account holder's name")
            self.balance = int(input("Enter the initial amount to be deposited in the account"))
            print("***ACCOUNT CREATED***")
            self.acc_List.append([self.accNo, self.name, self.balance])
            self.accNo_List.append(self.accNo)
        else:
            print("NOT AUTHORIZED")

    # Show Bank Account Details
    def showAccount(self, accno, role):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.accNo_List:
                print(self.accNo_List.index(accno))
                print("Account Number: ", self.acc_List[self.accNo_List.index(accno)][0])
                print("Account Holder Name:", self.acc_List[self.accNo_List.index(accno)][1])
                print("Account Balance:", self.acc_List[self.accNo_List.index(accno)][2])
        else:
            print("NOT AUTHORIZED")

    # Delete an Account from the Bank
    def deleteAccount(self, accno):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.accNo_List:
                temp = self.accNo_List.index(accno)
                self.acc_List.remove(self.acc_List[temp])
                self.accNo_List.remove(self.accNo_List[temp])
                print("YOUR ACCOUNT HAS BEEN CLOSED")
        else:
            print("NOT AUTHORIZED")

    # Modify Account Information (Only Name can be modified)
    def modifyAccount(self, accno):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.accNo_List:
                print(self.accNo_List.index(accno))
                print("*****MODIFY ACCOUNT DETAILS*****")
                print("NOTE : YOU CANNOT MODIFY ACCOUNT NUMBER")
                self.acc_List[self.accNo_List.index(accno)][1] = input("Enter Account Holder's Name")
                print("ACCOUNT INFO MODIFIED")
        else:
            print("NOT AUTHORIZED")

    # Load Lists back to CSV File
    def Bank_storeList(self):
        temp_accNo = []
        temp_accName = []
        temp_balance = []
        for i in self.acc_List:
            temp_accNo.append(i[0])
            temp_accName.append(i[1])
            temp_balance.append(i[2])
        data = {'AccNo': temp_accNo,
                'AccName': temp_accName,
                'AccBalance': temp_balance}
        to_df = pd.DataFrame(data, columns=['AccNo', 'AccName', 'AccBalance'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\BankTest.xlsx', sheet_name='BankClass', index=False, header=True)


# ********** BANK CLASS Ends **********
# ********** WALLET CLASS Starts **********
class Wallet(Bank):
    userData = {'Gopal': 'Father', 'Prema': 'Mother', 'Rishi': 'Child', 'Srinithi': 'Child'}
    wallet_acc_list = []
    wallet_balance = 0
    wallet_accNo_list = []

    def __init__(self):
        super().__init__()
        pass

    def Wallet_LoadList(self):
        dframe = pd.read_excel(r'C:\Users\Dell\Desktop\WalletTest.xlsx', sheet_name='WalletClass')
        from_df = pd.DataFrame(dframe,columns=['AccNo','AccName','AccBalance'])
        self.wallet_acc_list = from_df.values.tolist()

        balanceframe = pd.read_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx')
        from_df = pd.DataFrame(balanceframe,columns=['WalletBalance'])
        self.wallet_balance = int(from_df.values)

        for i in self.wallet_acc_list:
            self.wallet_accNo_list.append(i[0])

        transactionframe = pd.read_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx')
        from_df = pd.DataFrame(transactionframe,columns=['Transaction'])
        self.transaction_list = from_df.values.tolist()

    def addAccount(self, accno):
        if (role == 'Father') or (role == 'Mother'):
            if len(self.wallet_acc_list) == 2:
                print("Cannot add more than two accounts")
            else:
                print(self.acc_List)
                print("Account Number: ",
                      self.acc_List[self.accNo_List.index(accno)][0])  # print(b.acc_List[b.accNo_List.index(temp2)][0])
                print("Account Holder's Name: ", self.acc_List[self.accNo_List.index(accno)][1])
                print("Account Balance: ", self.acc_List[self.accNo_List.index(accno)][2])
                print("THIS BANK ACCOUNT HAS BEEN ADDED TO THE WALLET")
                self.wallet_acc_list.append(
                    [self.acc_List[self.accNo_List.index(accno)][0], self.acc_List[self.accNo_List.index(accno)][1],
                     self.acc_List[self.accNo_List.index(accno)][2]])
                self.wallet_accNo_list.append(self.acc_List[self.accNo_List.index(accno)][0])
                print(self.wallet_accNo_list)
        else:
            print("NOT AUTHORIZED")

    def removeAccount(self, accno):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.wallet_acc_list:
                self.wallet_acc_list.remove(
                    [self.acc_List[self.wallet_accNo_list.index(accno)][0], self.acc_List[self.wallet_accNo_list.index(accno)][1],
                     self.acc_List[self.wallet_accNo_list.index(accno)][2]])
                self.wallet_accNo_list.remove(self.wallet_accNo_list[self.wallet_accNo_list.index(accno)])
                print("BANK ACCOUNT {0} HAS BEEN REMOVED FROM THE WALLET ".format(accno))
            else:
                print("INCORRECT ACCOUNT NUMBER")
        else:
            print("NOT AUTHORIZED")

    def addMoneyToWallet(self, accno, amount):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.wallet_accNo_list:
                print(self.wallet_accNo_list.index(accno))
                if self.acc_List[self.accNo_List.index(accno)][2] < amount:
                    print("There is not enough balance in this account")
                else:
                    self.wallet_balance = self.wallet_balance + amount
                    self.acc_List[self.accNo_List.index(accno)][2] = self.acc_List[self.accNo_List.index(accno)][2] - amount
                    self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] = self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] - amount
                    print("CURRENT WALLET BALANCE: ", self.wallet_balance)
            else:
                print("ACCOUNT NUMBER NOT FOUND IN WALLET")
        else:
            print("NOT AUTHORIZED")

    def withdrawMoneyFromWallet(self, accno, amount):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.wallet_accNo_list:
                print(self.wallet_accNo_list.index(accno))
                if self.wallet_balance < amount:
                    print("There is not enough balance in wallet")
                else:
                    self.acc_List[self.accNo_List.index(accno)][2] = self.acc_List[self.accNo_List.index(accno)][2] + amount
                    self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] = self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] + amount
                    self.wallet_balance = self.wallet_balance - amount
                    print("CURRENT WALLET BALANCE: ", self.wallet_balance)
            else:
                print("ACCOUNT NUMBER NOT FOUND IN WALLET")
        else:
            print("NOT AUTHORIZED")

    def Wallet_storeList(self):
        temp_accNo = []
        temp_accName = []
        temp_balance = []
        for i in self.wallet_acc_list:
            temp_accNo.append(i[0])
            temp_accName.append(i[1])
            temp_balance.append(i[2])
        data = {'AccNo': temp_accNo,
                'AccName': temp_accName,
                'AccBalance': temp_balance}
        to_df = pd.DataFrame(data, columns=['AccNo', 'AccName', 'AccBalance'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\WalletTest.xlsx', sheet_name='WalletClass', index=False, header=True)

        balance_data = {'WalletBalance':self.wallet_balance}
        to_df = pd.DataFrame(balance_data,columns=['WalletBalance'],index=[0])
        to_df.to_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx', index=False, header=True)

        transaction_data = {'Transaction':self.transaction_list}
        to_df = pd.DataFrame(transaction_data,columns=['Transaction'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx', index=False, header=True)



# ********** WALLET CLASS Ends **********

# ********** DAD CLASS Starts **********
class User(Wallet):
    temp_itemName = []
    temp_itemPrice = []
    total_price = 0


    def __init__(self):
        super().__init__()
        pass
    def pay(self,shopName,amount,role,itemList):
        if (role == 'Child') and amount > 50:
            print("You cannot pay for transaction more than $ 50")
        else:
            for i in itemList:
                self.temp_itemName.append(i[0])
                self.temp_itemPrice.append(i[1])
            for i in self.temp_itemPrice:
                self.total_price = self.total_price + i
        self.transaction_list.append([shopName,self.temp_itemName,self.total_price,datetime.now().strftime('%Y-%m-%d''%H:%M:%S')])

# ********** DAD CLASS Ends **********

# ********** CLASSES Ends **********


# ********** MAIN CLASS **********

# ********** TEST BENCH - BANK and WALLET CLASS **********
# w.Bank_loadList()  # Load values from CSV
# w.Wallet_LoadList()
# print(w.wallet_acc_list)
# print(w.acc_List)
# print(w.wallet_balance)
# print("WALLET ACCOUNT LIST: ",w.wallet_accNo_list)
# # Bank Methods
# # w.createAccount()  # Create a New Account
# temp1 = int(input("Enter Account Number"))
# w.showAccount(temp1)  # View a New Account
# # temp1 = int(input("Enter Account Number"))
# # w.modifyAccount(temp1)
# # temp1 = int(input("Enter Account Number"))
# # w.deleteAccount(temp1)
# # Wallet Methods
# temp1 = int(input("Enter Account Number"))
# w.addAccount(temp1)
# temp1 = int(input("Enter Account Number"))
# w.addAccount(temp1)
# temp2 = int(input("Enter Account Number"))
# temp3 = int(input("Enter Amount"))
# w.addMoneyToWallet(temp2,temp3)
# print("WALLET BALANCE: ",w.wallet_balance)
# temp2 = int(input("Enter Account Number"))
# temp3 = int(input("Enter Amount"))
# w.withdrawMoneyFromWallet(temp2,temp3)
# print("WALLET BALANCE: ",w.wallet_balance)
#
# # temp1 = int(input("Enter Account Number"))
# # b.deleteAccount(temp1)  # delete account from Bank
# # temp1 = int(input("Enter Account Number"))
# # b.modifyAccount(temp1) # Modify Account
# # Store Values back to CSV
# w.Wallet_storeList()
# w.Bank_storeList()
# # w.Wallet_storeList()

# MAIN CLASS TEST
b = Bank()  # Bank Class Object
w = Wallet()  # Wallet Class Object
w.Bank_loadList()  # Load values from CSV
w.Wallet_LoadList()

while True:
    print("WELCOME TO FAMILY WALLET")
    username = input("Please Enter your user name")
    if username in w.userData.keys():
        print("VALID USER")
        break
    else:
        print("INVALID USER, TRY AGAIN")
role = w.userData.get(username)
print(role)
temp1 = int(input("Enter Account number"))
w.showAccount(temp1,role)

w.Bank_storeList()
w.Wallet_storeList()








