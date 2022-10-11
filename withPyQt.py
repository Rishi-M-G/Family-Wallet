# ********** IMPORTS **********
from datetime import datetime
import sys
import csv
import pandas as pd
# ********** IMPORTS **********

# ********** CLASSES **********
# ********** BANK CLASS **********
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
    def loadList(self):
        dframe = pd.read_csv("C:\\Users\\Dell\\Desktop\\WalletTest.csv")
        from_df = pd.DataFrame(dframe)
        self.acc_List = from_df['acc_List'].values.tolist()
        self.accNo_List = from_df['accNo_List'].values.tolist()
        self.transaction_list = from_df['transaction_list'].values.tolist()
        print(self.acc_List)
        print(self.acc_List[0])
        print(self.accNo_List)

    def createAccount(self):
        print(self.acc_List)
        self.accNo = int(input("Enter the desired bank account number"))
        self.name = input("Enter the account holder's name")
        self.balance = int(input("Enter the initial amount to be deposited in the account"))
        print("***ACCOUNT CREATED***")
        self.acc_List.append([self.accNo, self.name, self.balance])
        self.accNo_List.append(self.accNo)

    def storeList(self):
        data = {'acc_List':self.acc_List,
                'accNo_List':self.accNo_List,
                'transaction_List':self.transaction_list}
        to_df = pd.DataFrame(data,columns=['acc_List','accNo_List','transaction_list'])
        to_df.to_csv(r'C:\Users\Dell\Desktop\WalletTest.csv',index=False,header=True)


# ********** BANK CLASS **********
# ********** CLASSES **********

# ********** MAIN CLASS **********
b = Bank()
b.loadList()
