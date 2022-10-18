# ********** IMPORTS Starts **********
from datetime import datetime
import sys
import csv
import pandas as pd
import openpyxl
import shutil
columns = shutil.get_terminal_size().columns
from termcolor import colored

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
        dframe = pd.read_excel('BankTest.xlsx', sheet_name='BankClass')
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
            print("***ACCOUNT CREATED***".center(columns))
            self.acc_List.append([self.accNo, self.name, self.balance])
            self.accNo_List.append(self.accNo)
        else:
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns),'red'))

    # Show Bank Account Details
    def showAccount(self, accno, role):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.accNo_List:
                print("Account Number: ".center(columns), self.acc_List[self.accNo_List.index(accno)][0])
                print("Account Holder Name:".center(columns), self.acc_List[self.accNo_List.index(accno)][1])
                print("Account Balance:".center(columns), self.acc_List[self.accNo_List.index(accno)][2])
            else:
                print(colored("ACCOUNT NUMBER : {0} NOT FOUND".format(accno).center(columns), 'red'))
        else:
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns),'red'))

    # Delete an Account from the Bank
    def deleteAccount(self, accno,role):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.accNo_List:
                temp = self.accNo_List.index(accno)
                self.acc_List.remove(self.acc_List[temp])
                self.accNo_List.remove(self.accNo_List[temp])
                print("YOUR ACCOUNT HAS BEEN CLOSED")
        else:
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns),'red'))

    # Modify Account Information (Only Name can be modified)
    def modifyAccount(self, accno,role):
        if (role == 'Father') or (role == 'Mother'):
            if accno in self.accNo_List:
                print(self.accNo_List.index(accno))
                print("*****MODIFY ACCOUNT DETAILS*****".center(columns))
                print("NOTE : YOU CANNOT MODIFY ACCOUNT NUMBER".center(columns))
                self.acc_List[self.accNo_List.index(accno)][1] = input("Enter Account Holder's Name")
                print("ACCOUNT INFO MODIFIED".center(columns))
        else:
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns),'red'))

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
        to_df.to_excel('BankTest.xlsx', sheet_name='BankClass', index=False, header=True)


# ********** BANK CLASS Ends **********
# ********** WALLET CLASS Starts **********
class Wallet(Bank):
    userData = {'Gopal': 'Father', 'Prema': 'Mother', 'Rishi': 'Child', 'Srinithi': 'Child','Siva':'Child','Sabareesh':'Child','Yuga':'Child','Gnana':'Child','Prithvi':'Child','Pranav':'Child'}
    countData = {'Gopal':0,'Prema':0,'Rishi':0,'Srinithi':0,'Siva':0,'Sabareesh':0,'Yuga':0,'Gnana':0,'Prithivi':0,'Pranav':0}
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
        dframe = pd.read_excel('WalletTest.xlsx', sheet_name='WalletClass')
        from_df = pd.DataFrame(dframe, columns=['AccNo', 'AccName', 'AccBalance'])
        self.wallet_acc_list = from_df.values.tolist()


        balanceframe = pd.read_excel('WalletBalance.xlsx')
        from_df = pd.DataFrame(balanceframe, columns=['WalletBalance'])
        self.wallet_balance = int(from_df.values)

        for i in self.wallet_acc_list:
            self.wallet_accNo_list.append(i[0])

        transactionframe = pd.read_excel('Transaction.xlsx')
        from_df = pd.DataFrame(transactionframe, columns=['Transaction'])
        self.transaction_list = from_df.values.tolist()

        dadnotificationframe = pd.read_excel('DadNotificationList.xlsx')
        from_df = pd.DataFrame(dadnotificationframe,columns=['Message','Role'])
        self.dad_notification_List = from_df.values.tolist()

        momnotificationframe = pd.read_excel('MomNotificationList.xlsx')
        from_df = pd.DataFrame(momnotificationframe,columns=['Message','Role'])
        self.mom_notification_List = from_df.values.tolist()

        permissiondataframe = pd.read_excel('Permission.xlsx')
        from_df = pd.DataFrame(permissiondataframe,columns=['Gopal','Prema','Rishi','Srinithi','Siva','Sabareesh','Yuga','Gnana','Prithvi','Pranav'])
        self.permission_list = from_df.values.tolist()

        blockeddataframe = pd.read_excel('BlockedList.xlsx')
        from_df = pd.DataFrame(blockeddataframe,columns=['BlockedList'])
        self.blocked_list = from_df.values.tolist()

        overspenddataframe = pd.read_excel('OverSpend.xlsx')
        from_df = pd.DataFrame(overspenddataframe, columns=['Gopal','Prema','Rishi','Srinithi','Siva','Sabareesh','Yuga','Gnana','Prithvi','Pranav'])
        self.overspend_list = from_df.values.tolist()

        # countdataframe = pd.read_excel(r'C:\Users\Dell\Desktop\Count.xlsx')
        # from_df = pd.DataFrame(countdataframe,columns=['Rishi','Srinithi'])
        # self.countData = from_df.values

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
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns),'red'))

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
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns),'red'))

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
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns),'red'))

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
            print(colored("{0} NOT AUTHORIZED".format(role).center(columns)),'red')


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
        to_df.to_excel('WalletTest.xlsx', sheet_name='WalletClass', index=False, header=True)

        balance_data = {'WalletBalance': self.wallet_balance}
        to_df = pd.DataFrame(balance_data, columns=['WalletBalance'], index=[0])
        to_df.to_excel('WalletBalance.xlsx', index=False, header=True)

        transaction_data = {'Transaction': self.transaction_list}
        to_df = pd.DataFrame(transaction_data, columns=['Transaction'])
        to_df.to_excel('Transaction.xlsx', index=True, header=True)

        for i in self.mom_notification_List:
            temp_mom_message.append(i[0])
            temp_mom_role.append(i[1])
        momnotification_data = {'Message':temp_mom_message,'Role':temp_mom_role}
        to_df =pd.DataFrame(momnotification_data,columns=['Message','Role'])
        to_df.to_excel('MomNotificationList.xlsx',index=False,header=True)

        for i in self.dad_notification_List:
            temp_dad_message.append(i[0])
            temp_dad_role.append(i[1])
        dadnotification_data = {'Message':temp_dad_message,'Role':temp_dad_role}
        to_df =pd.DataFrame(dadnotification_data,columns=['Message','Role'])
        to_df.to_excel('DadNotificationList.xlsx',index=False,header=True)

        permission_data = {'Gopal':self.permission_list[0][0],'Prema':self.permission_list[0][1],'Rishi':self.permission_list[0][2],'Srinithi':self.permission_list[0][3],'Siva':self.permission_list[0][4],'Sabareesh':self.permission_list[0][5],'Yuga':self.permission_list[0][6],'Gnana':self.permission_list[0][7],'Prithvi':self.permission_list[0][8],'Pranav':self.permission_list[0][9]}
        to_df = pd.DataFrame(permission_data,columns=['Gopal','Prema','Rishi','Srinithi','Siva','Sabareesh','Yuga','Gnana','Prithvi','Pranav'],index=[0])
        to_df.to_excel('Permission.xlsx',index=False,header=True)

        blocked_data = {'BlockedList':self.blocked_list}
        to_df = pd.DataFrame(blocked_data,columns=['BlockedList'])
        to_df.to_excel('BlockedList.xlsx',index=False,header=True)

        overspend_data = {'Gopal':self.overspend_list[0][0],'Prema':self.overspend_list[0][1],'Rishi':self.overspend_list[0][2],'Srinithi':self.overspend_list[0][3],'Siva':self.overspend_list[0][4],'Sabareesh':self.overspend_list[0][5],'Yuga':self.overspend_list[0][6],'Gnana':self.overspend_list[0][7],'Prithvi':self.overspend_list[0][8],'Pranav':self.overspend_list[0][9]}
        to_df = pd.DataFrame(overspend_data, columns=['Gopal','Prema','Rishi','Srinithi','Siva','Sabareesh','Yuga','Gnana','Prithvi','Pranav'],index=[0])
        to_df.to_excel('OverSpend.xlsx', index=False, header=True)

        # count_data = {'Rishi':self.count_list[0],'Srinithi':self.count_list[1]}
        # to_df = pd.DataFrame(count_data,columns=['Rishi','Srinithi'])
        # to_df.to_excel(r'C:\Users\Dell\Desktop\Count.xlsx', index=False, header=True)


    def endOfTheDay(self):
        source_datetime = datetime.datetime.now()
        eod = datetime.datetime(
            year=source_datetime.year,
            month=source_datetime.month,
            day=source_datetime.day
        ) + datetime.timedelta(days=1, microseconds=-1)
        return eod

    def endOfTheDayUpdations(self, eod,username):
        if datetime.datetime.now() == eod:
            count = 0
            countData = {username: count}
            self.countData.update(countData)



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
                self.total_price = self.total_price + i
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
            temp_list = []
            for i in self.dad_notification_List:
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
        self.wallet_balance = self.wallet_balance - totalprice





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
user = User()
user.Bank_loadList()  # Load values from CSV
user.Wallet_LoadList()
print("WELCOME TO FAMILY WALLET".center(columns))
while True:
    username = input("Please Enter your user name".center(columns))
    passcode = int(input("Enter Passcode".center(columns)))
    if username in user.userData.keys():
        if username in user.blocked_list:
            print("********** YOU HAVE BEEN BLOCKED **********".center(columns))
        else:
            print("Welcome..! You are a Valid User".center(columns))
        break
    else:
        print("********** INVALID USER, TRY AGAIN **********".center(columns))
print("************************************************************".center(columns))
role = user.userData.get(username)
userIndex = list(user.userData.keys()).index(username)
if username in user.blocked_list:
    print("Blocked")
permission = user.permission_list[0][userIndex]
overspend = user.overspend_list[0][userIndex]
print("WHAT DO YOU WANT TO ACCESS?".center(columns))
print("1.Bank".center(columns))
print("2.Wallet".center(columns))
choice = int(input())
if choice == 1:
    while True:
        print("******************** WELCOME TO THE BANK ********************".center(columns))
        print("Account List:", user.acc_List)
        print("********** HOW CAN WE HELP YOU ? **********".center(columns))
        print("1.Create Account".center(columns))
        print("2.Show Account Details".center(columns))
        print("3.Delete Account".center(columns))
        print("4.Modify Account Name".center(columns))
        print("5.Exit Bank".center(columns))
        choice = int(input())
        if choice == 1:
            print("********** CREATING AN ACCOUNT **********".center(columns))
            user.createAccount(role)
        elif choice == 2:
            print("********** SHOW ACCOUNT DETAILS **********".center(columns))
            accountNumber = int(input("Enter Account Number".center(columns)))
            user.showAccount(accountNumber,role)
        elif choice == 3:
            print("********** DELETE ACCOUNT **********".center(columns))
            accountNumber = int(input("Enter Account Number".center(columns)))
            user.deleteAccount(accountNumber,role)
        elif choice == 4:
            print("********** MODIFY ACCOUNT **********".center(columns))
            accountNumber = int(input("Enter Account Number".center(columns)))
            user.modifyAccount(accountNumber,role)
        elif choice == 5:
            break
        else:
            print("********** INVALID CHOICE **********".center(columns))
elif choice == 2:
    while True:
        print("******************** WELCOME TO THE BANK ********************".center(columns))
        print("Wallet Account List : ", user.wallet_acc_list)
        print("\n")
        print("-----------------------------------------------------------------------".center(columns))
        print("WALLET BALANCE : ".center(columns),user.wallet_balance)
        print("-----------------------------------------------------------------------".center(columns))
        print("\n")
        print("********** HOW CAN WE HELP YOU ? **********".center(columns))
        print("1.Add Account to Wallet".center(columns))
        print("2.Remove Account to Wallet".center(columns))
        print("3.Add Money From Wallet".center(columns))
        print("4.Send Money From Wallet to Bank".center(columns))
        print("5.Pay".center(columns))
        print("6.View Transactions".center(columns))
        print("7.Block User".center(columns))
        print("8.Unblock User".center(columns))
        print("9.View Notifications".center(columns))
        print("10.Exit".center(columns))
        choice = int(input())
        if choice == 1:
            print("********** ADDING ACCOUNT TO WALLET **********".center(columns))
            accountNumber = int(input("Enter Account Number".center(columns)))
            user.addAccount(accountNumber,role)
        elif choice == 2:
            print("********** REMOVING ACCOUNT FROM WALLET **********".center(columns))
            accountNumber = int(input("Enter Account Number".center(columns)))
            user.removeAccount(accountNumber,role)
        elif choice == 3:
            print("********** ADDING MONEY TO WALLET **********".center(columns))
            accountNumber = int(input("Enter Account Number".center(columns)))
            amount = int(input("Enter Amount".center(columns)))
            user.addMoneyToWallet(accountNumber,amount,role)
        elif choice == 4:
            print("********** SENDING MONEY FROM WALLET TO BANK **********".center(columns))
            accountNumber = int(input("Enter Account Number".center(columns)))
            amount = int(input("Enter Amount".center(columns)))
            user.withdrawMoneyFromWallet(accountNumber,amount,role,username)
        elif choice == 5:
            print("********** PAY TO BUSINESS **********".center(columns))
            ShopName = input("Enter Shop Name".center(columns))
            itemCount = int(input("Enter Number of Items".center(columns)))
            tempItemList = []
            for i in range(0,itemCount):
                name = input("Enter Item Name".center(columns))
                price = int(input("Enter Item Price".center(columns)))
                tempItemList.append([name,price])
            user.pay(ShopName,role,tempItemList,username,permission,overspend)
        elif choice == 6:
            print("********** VIEWING TRANSACTIONS **********".center(columns))
            user.viewTransaction(role)
        elif choice == 7:
            print("********** BLOCK USER **********".center(columns))
            user.blockUser(role)
        elif choice == 8:
            print("********** UNBLOCK USER **********".center(columns))
            user.unblockUser(role)
        elif choice == 9:
            print("********** NOTIFICATIONS **********".center(columns))
            user.viewNotifications(role)
        elif choice == 10:
            break
        else:
            print("********** INVALID CHOICE **********".center(columns))
user.endOfTheDay()
user.endOfTheDayUpdations()
user.Bank_storeList()
user.Wallet_storeList()

