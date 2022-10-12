# import openpyxl
# import pandas as pd
# dframe = pd.read_excel(r'C:\Users\Dell\Desktop\WalletTest.xlsx',sheet_name='WalletClass')
# from_df = pd.DataFrame(dframe)
# testList = from_df.values
# testList = testList.tolist()
# print(testList)
# print(type(testList))
# print(testList[0][1])
# print(type(testList[0][1]))
#
# testList.append([1003,'Bhavya',3000])
#
# temp_accNo = []
# temp_accName = []
# temp_accBalace = []
# for i in testList:
#     temp_accNo.append(i[0])
#     temp_accName.append(i[1])
#     temp_accBalace.append(i[2])
#
# data = {'AccNo':temp_accNo,
#         'AccName':temp_accName,
#         'AccBalance':temp_accBalace}
# to_df = pd.DataFrame(data,columns=['AccNo','AccName','AccBalance'])
# to_df.to_excel(r'C:\Users\Dell\Desktop\WalletTest.xlsx',sheet_name='WalletClass',index=False,header=True)
#
#
