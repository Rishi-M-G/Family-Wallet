import pandas as pd

wallet_acc_list = []
def Wallet_LoadList():
    dframe = pd.read_excel('Book1.xlsx')
    from_df = pd.DataFrame(dframe, columns=['AccNo', 'AccName', 'AccBalance'])
    wallet_acc_list = from_df.values.tolist()


def Wallet_storeList():
    temp_accNo = []
    temp_accName = []
    temp_balance = []
    temp_mom_message = []
    temp_mom_role = []
    temp_dad_message = []
    temp_dad_role = []

    for i in wallet_acc_list:
        temp_accNo.append(i[0])
        temp_accName.append(i[1])
        temp_balance.append(i[2])
    data = {'AccNo': temp_accNo,
            'AccName': temp_accName,
            'AccBalance': temp_balance}
    to_df = pd.DataFrame(data, columns=['AccNo', 'AccName', 'AccBalance'])
    to_df.to_excel('Book1.xlsx',index=False)


wallet_acc_list.append([1001,'Rishi',500])

Wallet_storeList()
