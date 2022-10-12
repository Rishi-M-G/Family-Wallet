# *********** BANK CLASS ********
class Bank:
    accNo = None
    balance = None
    name = None
    acc_List = []
    accNo_List = []

    def __init__(self):
        pass

    def createAccount(self):
        self.accNo = int(input("Enter the desired bank account number"))
        self.name = input("Enter the account holder's name")
        self.balance = int(input("Enter the initial amount to be deposited in the account"))
        print("***ACCOUNT CREATED***")
        return [self.accNo, self.name, self.balance]

    def showAccount(self, list_arg):
        for i in list_arg:
            self.accNo_List.append(i[0])
        self.temp1 = int(input("Enter Account Number:"))
        if self.temp1 in self.accNo_List:
            print(self.accNo_List.index(self.temp1))
            print("Account Number: ", list_arg[self.accNo_List.index(self.temp1)][0])
            print("Account Holder Name:", list_arg[self.accNo_List.index(self.temp1)][1])
            print("Account Balance:", list_arg[self.accNo_List.index(self.temp1)][2])

    def deleteAccount(self,list_arg):
        for i in list_arg:
            self.accNo_List.append(i[0])
        self.temp1 = int(input("Enter Account Number:"))
        if self.temp1 in self.accNo_List:
            print(self.accNo_List.index(self.temp1))
            list_arg.remove(list_arg[self.accNo_List.index(self.temp1)])
            return list_arg

    def modifyAccount(self,list_arg):
        for i in list_arg:
            self.accNo_List.append(i[0])
        self.temp1 = int(input("Enter Account Number:"))
        if self.temp1 in self.accNo_List:
            print(self.accNo_List.index(self.temp1))
            print("*****MODIFY ACCOUNT DETAILS*****")
            print("NOTE : YOU CANNOT MODIFY ACCOUNT NUMBER")
            list_arg[self.accNo_List.index(self.temp1)][1] = input("Enter Account Holder's Name")
            return list_arg

# ************* MAIN WINDOW *************

# Creating Bank Accounts List
list1 = []

# CreateAccount() Method Call
list1.append(Bank().createAccount())
# list1.append(Bank().createAccount())

# Dummy Values for testing
list1.append([1004, 'Rishi', 1000])

print(list1[0])
print(list1[1])
print("Account Number:{0}   Name:{1}   Balance:{2}".format(list1[0][0], list1[0][1], list1[0][2]))

# ShowAccount() method call
Bank().showAccount(list1)

# DeleteAccount() Method Call
# list1 = Bank().deleteAccount(list1)
# print(list1)

# modifyAccount() Method Call
list1 = Bank().modifyAccount(list1)
print(list1)