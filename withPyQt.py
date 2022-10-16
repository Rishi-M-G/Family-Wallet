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
    def createAccount(self, role):
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
    countData = {'Gopal':0,'Prema':0,'Rishi':0,'Srinithi':0}
    blocked_list = []
    dad_notification_List = []
    mom_notification_List = []
    wallet_acc_list = []
    wallet_balance = 0
    wallet_accNo_list = []
    permission_list=[]
    overspend_list=[]

    def __init__(self):
        super().__init__()
        pass

    def Wallet_LoadList(self):
        dframe = pd.read_excel(r'C:\Users\Dell\Desktop\WalletTest.xlsx', sheet_name='WalletClass')
        from_df = pd.DataFrame(dframe, columns=['AccNo', 'AccName', 'AccBalance'])
        self.wallet_acc_list = from_df.values.tolist()

        balanceframe = pd.read_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx')
        from_df = pd.DataFrame(balanceframe, columns=['WalletBalance'])
        self.wallet_balance = int(from_df.values)

        for i in self.wallet_acc_list:
            self.wallet_accNo_list.append(i[0])

        transactionframe = pd.read_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx')
        from_df = pd.DataFrame(transactionframe, columns=['Transaction'])
        self.transaction_list = from_df.values.tolist()

        dadnotificationframe = pd.read_excel(r'C:\Users\Dell\Desktop\DadNotificationList.xlsx')
        from_df = pd.DataFrame(dadnotificationframe,columns=['Message','Role'])
        self.dad_notification_List = from_df.values.tolist()

        momnotificationframe = pd.read_excel(r'C:\Users\Dell\Desktop\MomNotificationList.xlsx')
        from_df = pd.DataFrame(momnotificationframe,columns=['Message','Role'])
        self.mom_notification_List = from_df.values.tolist()

        permissiondataframe = pd.read_excel(r'C:\Users\Dell\Desktop\Permission.xlsx')
        from_df = pd.DataFrame(permissiondataframe,columns=['Rishi','Srinithi'])
        self.permission_list = from_df.values.tolist()

        blockeddataframe = pd.read_excel(r'C:\Users\Dell\Desktop\BlockedList.xlsx')
        from_df = pd.DataFrame(blockeddataframe,columns=['BlockedList'])
        self.blocked_list = from_df.values.tolist()

        overspenddataframe = pd.read_excel(r'C:\Users\Dell\Desktop\OverSpend.xlsx')
        from_df = pd.DataFrame(overspenddataframe, columns=['Rishi','Srinithi'])
        self.overspend_list = from_df.values.tolist()

    def addAccount(self, accno, role):
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

    def removeAccount(self, accno,role):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.wallet_acc_list:
                self.wallet_acc_list.remove(
                    [self.acc_List[self.wallet_accNo_list.index(accno)][0],
                     self.acc_List[self.wallet_accNo_list.index(accno)][1],
                     self.acc_List[self.wallet_accNo_list.index(accno)][2]])
                self.wallet_accNo_list.remove(self.wallet_accNo_list[self.wallet_accNo_list.index(accno)])
                print("BANK ACCOUNT {0} HAS BEEN REMOVED FROM THE WALLET ".format(accno))
            else:
                print("INCORRECT ACCOUNT NUMBER")
        else:
            print("NOT AUTHORIZED")

    def addMoneyToWallet(self, accno, amount,role):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.wallet_accNo_list:
                print(self.wallet_accNo_list.index(accno))
                if self.acc_List[self.accNo_List.index(accno)][2] < amount:
                    print("There is not enough balance in this account")
                else:
                    self.wallet_balance = self.wallet_balance + amount
                    self.acc_List[self.accNo_List.index(accno)][2] = self.acc_List[self.accNo_List.index(accno)][
                                                                         2] - amount
                    self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] = \
                        self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] - amount
                    print("CURRENT WALLET BALANCE: ", self.wallet_balance)
            else:
                print("ACCOUNT NUMBER NOT FOUND IN WALLET")
        else:
            print("NOT AUTHORIZED")

    def withdrawMoneyFromWallet(self, accno, amount, role,username):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.wallet_accNo_list:
                print(self.wallet_accNo_list.index(accno))
                if self.wallet_balance < amount:
                    print("There is not enough balance in wallet")
                else:
                    self.acc_List[self.accNo_List.index(accno)][2] = self.acc_List[self.accNo_List.index(accno)][
                                                                         2] + amount
                    self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] = \
                        self.wallet_acc_list[self.wallet_accNo_list.index(accno)][2] + amount
                    self.wallet_balance = self.wallet_balance - amount
                    print("CURRENT WALLET BALANCE: ", self.wallet_balance)
                    if self.wallet_balance < 100:
                        self.dad_notification_List.append(["Wallet Balance is less than $ 100", username])
                        self.mom_notification_List.append(["Wallet Balance is less than $ 100", username])
            else:
                print("ACCOUNT NUMBER NOT FOUND IN WALLET")
        else:
            print("NOT AUTHORIZED")


    def Wallet_storeList(self):
        temp_accNo = []
        temp_accName = []
        temp_balance = []
        temp_mom_message = []
        temp_mom_role =[]
        temp_dad_message = []
        temp_dad_role = []

        for i in self.wallet_acc_list:
            temp_accNo.append(i[0])
            temp_accName.append(i[1])
            temp_balance.append(i[2])
        data = {'AccNo': temp_accNo,
                'AccName': temp_accName,
                'AccBalance': temp_balance}
        to_df = pd.DataFrame(data, columns=['AccNo', 'AccName', 'AccBalance'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\WalletTest.xlsx', sheet_name='WalletClass', index=False, header=True)

        balance_data = {'WalletBalance': self.wallet_balance}
        to_df = pd.DataFrame(balance_data, columns=['WalletBalance'], index=[0])
        to_df.to_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx', index=False, header=True)

        transaction_data = {'Transaction': self.transaction_list}
        to_df = pd.DataFrame(transaction_data, columns=['Transaction'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\WalletBalance.xlsx', index=False, header=True)

        for i in self.mom_notification_List:
            temp_mom_message.append(i[0])
            temp_mom_role.append(i[1])
        momnotification_data = {'Message':temp_mom_message,'Role':temp_mom_role}
        to_df =pd.DataFrame(momnotification_data,columns=['Message','Role'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\MomNotificationList.xlsx',index=False,header=True)

        for i in self.dad_notification_List:
            temp_dad_message.append(i[0])
            temp_dad_role.append(i[1])
        dadnotification_data = {'Message':temp_dad_message,'Role':temp_dad_role}
        to_df =pd.DataFrame(dadnotification_data,columns=['Message','Role'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\DadNotificationList.xlsx',index=False,header=True)

        permission_data = {'Rishi':self.permission_list[0],'Srinithi':self.permission_list[1]}
        to_df = pd.DataFrame(permission_data,columns=['Rishi','Srinithi'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\Permission.xlsx',index=False,header=True)

        blocked_data = {'BlockedList':self.blocked_list}
        to_df = pd.DataFrame(blocked_data,columns=['BlockedList'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\Permission.xlsx',index=False,header=True)

        overspend_data = {'OverSpend': self.overspend_list}
        to_df = pd.DataFrame(overspend_data, columns=['Rishi','Srinithi'])
        to_df.to_excel(r'C:\Users\Dell\Desktop\OverSpend.xlsx', index=False, header=True)

        def endOfTheDay(self):
            source_datetime = datetime.datetime.now()
            eod = datetime.datetime(
                year=source_datetime.year,
                month=source_datetime.month,
                day=source_datetime.day
            ) + datetime.timedelta(days=1, microseconds=-1)
            return eod

        def endOfTheDayUpdations(self, eod):
            if datetime.datetime.now() == eod:
                self.c


# ********** WALLET CLASS Ends **********

# ********** DAD CLASS Starts **********
class User(Wallet):
    temp_itemName = []
    temp_itemPrice = []
    total_price = 0

    def __init__(self):
        super().__init__()
        pass

    # def pay(self, shopName, amount, role, itemList, username,permission,overspend):
    #     count = self.countData.get(username)
    #     if(role == 'Child') and (permission == 'Granted'):
    #         for i in itemList:
    #             self.temp_itemName.append(i[0])
    #             self.temp_itemPrice.append(i[1])
    #         for i in self.temp_itemPrice:
    #             self.total_price = self.total_price + i[1]
    #         self.transaction_list.append(
    #             [username, shopName, self.temp_itemName, self.total_price,
    #              datetime.now().strftime('%Y-%m-%d''%H:%M:%S')])
    #         count = count + 1
    #         countData = {username: count}
    #         self.countData.update(countData)
    #         self.wallet_balance = self.wallet_balance - self.total_price
    #         if self.wallet_balance < 100:
    #             self.balanceIsLess(username)
    #             # self.dad_notification_List.append(["Wallet Balance is less than $ 100", username])
    #             # self.mom_notification_List.append(["Wallet Balance is less than $ 100", username])
    #     else:
    #         if (role == 'Child') and count > 1:
    #             print("You cannot make more than 1 transaction per day")
    #             temp = input('Do you want to request Dad or Mom for more transactions? Yes / No')
    #             if temp == 'Yes':
    #                 self.requestTransactions(role, username)
    #                 print("Request Sent")
    #             else:
    #                 pass
    #         else:
    #             if (role == 'Child') and amount > 50 and overspend == 'Not Allowed':
    #                 print("You cannot pay for transaction more than $ 50")
    #                 self.spendMoreThan50(role,username)
    #             else:
    #                 for i in itemList:
    #                     self.temp_itemName.append(i[0])
    #                     self.temp_itemPrice.append(i[1])
    #                 for i in self.temp_itemPrice:
    #                     self.total_price = self.total_price + i
    #                 self.transaction_list.append(
    #                     [username, shopName, self.temp_itemName, self.total_price, datetime.now().strftime('%Y-%m-%d''%H:%M:%S')])
    #                 count = count + 1
    #                 countData = {username:count}
    #                 self.countData.update(countData)
    #                 if self.wallet_balance < 100:
    #                     self.balanceIsLess(username)
    #                     # self.dad_notification_List.append(["Wallet Balance is less than $ 100",username])
    #                     # self.mom_notification_List.append(["Wallet Balance is less than $ 100",username])

    def pay(self,shopName,role,itemList,username,permission,overspend):
        count = self.countData.get(username)
        if role == 'Child' and count > 0:
            print("You cannot make more than 1 transaction per day")
            temp = input('Do you want to request Dad or Mom for more transactions? Yes / No')
            if temp == 'Yes':
                self.requestTransactions(role, username)
                print("Request Sent")
            else:
                pass
        elif (role == 'Child' and count == 0) or (role == 'Father' or role == 'Mother'):
            for i in itemList:
                self.temp_itemName.append(i[0])
                self.temp_itemPrice.append(i[1])
            for i in self.temp_itemPrice:
                self.total_price = self.total_price + i[1]
            if self.total_price > 50 and overspend == 'Not Allowed' and role == 'Child':
                print("You cannot spend more than $50")
                self.spendMoreThan50(role,username)
            else:
                self.successfulTransaction(username, shopName, self.temp_itemName, self.total_price)
                count = count + 1
                countData = {username:count}
                self.countData.update(countData)
                if self.wallet_balance < 100:
                    self.balanceIsLess(username)
    def viewTransaction(self, role):
        if (role == 'Father') or (role == 'Mother'):
            print("******************** Transaction List ********************")
            print(self.transaction_list)
            print("**********************************************************")
        else:
            print("NOT AUTHORIZED")

    def blockUser(self, role):
        if role == 'Father':
            self.blocked_list.append(input("Enter username to be blocked"))
            print("User has been blocked")
        else:
            print('You are not authorized to block any Users')

    def unblockUser(self, role):
        if role == 'Father':
            self.blocked_list.remove(input("Enter username to be unblocked"))
            print("User has been unblocked")
        else:
            print('You are not authorized to block any Users')

    def viewNotifications(self,role):
        if role == 'Father':
            for i in self.dad_notification_List:
                temp_list = []
                temp_list.append(i)
            for i in temp_list:
                print("""Message: {0}   By:{1}""".format(i[0],i[1]))
                temp = input("Do you want to respond to the notification? Yes / No")
                if(temp == 'Yes') and (i[0] == "I want to make more transactions"):
                    userIndex = list(self.userData.keys()).index(i[1])
                    self.permission_list[userIndex] = "Granted"
                    self.dad_notification_List.remove(i)
                elif(temp == 'Yes') and (i[0] == "Wallet Balance is 0"):
                    accno = int(input("Enter Account Number"))
                    amount = int(input("Enter Amount"))
                    self.addMoneyToWallet(accno,amount,role)
                    self.dad_notification_List.remove(i)
                elif(temp == 'Yes') and (i[0] == "Wallet Balance is less than $ 100"):
                    accno = int(input("Enter Account Number"))
                    amount = int(input("Enter Amount"))
                    self.addMoneyToWallet(accno, amount, role)
                    self.dad_notification_List.remove(i)
                elif(temp == 'Yes') and (i[0] == "I want to spend more than 50 dollars"):
                    decision = input("Do you want to take this request or transfer it ? Take / Leave")
                    if decision == 'Take':
                        userIndex = list(self.userData.keys()).index(i[1])
                        self.overspend_list[userIndex] = "Allow"
                        self.dad_notification_List.remove(i)
                    if decision == 'Leave':
                        pass
                else:
                    continue
        if role == 'Mother':
            for i in self.mom_notification_List:
                temp_list = []
                temp_list.append(i)
            for i in temp_list:
                print("""Message: {0}   By:{1}""".format(i[0], i[1]))
                temp = input("Do you want to respond to the notification? Yes / No")
                if (temp == 'Yes') and (i[0] == "I want to make more transactions"):
                    userIndex = list(self.userData.keys()).index(i[1])
                    self.permission_list[userIndex] = "Granted"
                    self.mom_notification_List.remove(i)
                elif (temp == 'Yes') and (i[0] == "Wallet Balance is 0"):
                    accno = int(input("Enter Account Number"))
                    amount = int(input("Enter Amount"))
                    self.addMoneyToWallet(accno, amount, role)
                    self.mom_notification_List.remove(i)
                elif (temp == 'Yes') and (i[0] == "Wallet Balance is less than $ 100"):
                    accno = int(input("Enter Account Number"))
                    amount = int(input("Enter Amount"))
                    self.addMoneyToWallet(accno, amount, role)
                    self.mom_notification_List.remove(i)
                elif (temp == 'Yes') and (i[0] == "I want to spend more than 50 dollars"):
                    decision = input("Do you want to take this request or transfer it ? Take / Transfer" )
                    if decision == 'Take':
                        userIndex = list(self.userData.keys()).index(i[1])
                        self.overspend_list[userIndex] = "Allow"
                        self.mom_notification_List.remove(i)
                    if decision == 'Transfer':
                        userIndex = list(self.userData.keys()).index(i[1])
                        self.dad_notification_List.append(["I want to spend more than 50 dollars",i[1]])
                else:
                    continue

    def balanceIsZero(self,role,username):
        if role == 'Child':
            if self.wallet_balance == 0:
                self.dad_notification_List.append(["Wallet Balance is 0",username])
                self.mom_notification_List.append(["Wallet Balance is 0",username])

    def requestTransactions(self,role,username):
        if role == 'Child':
            self.dad_notification_List.append(["I want to make more transactions",username])
            self.mom_notification_List.append(["I want to make more transactions",username])

    def balanceIsLess(self,username):
        self.dad_notification_List.append(["Wallet Balance is less than $ 100", username])
        self.mom_notification_List.append(["Wallet Balance is less than $ 100", username])

    def spendMoreThan50(self,role,username):
        if role == 'Child':
            temp = input("Do you want to request Mom to allow transaction more than $50? Yes / No")
            if temp == 'Yes':
                self.mom_notification_List.append(["I want to spend more than 50 dollars", username])
                print("Request Sent")

    def successfulTransaction(self,username,shopName,item,totalprice):
        self.transaction_list.append([username, shopName,item,totalprice, datetime.now().strftime('%Y-%m-%d''%H:%M:%S')])
        print("SUCCESSFUL TRANSACTION")





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
        if username in w.blocked_list:
            print("You have been blocked")
        else:
            print("Valid User")
        break
    else:
        print("INVALID USER, TRY AGAIN")
role = w.userData.get(username)
print(role)
temp1 = int(input("Enter Account number"))
w.showAccount(temp1, role)

w.Bank_storeList()
w.Wallet_storeList()
