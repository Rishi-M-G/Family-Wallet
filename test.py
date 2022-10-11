import csv

import pandas as pd

dframe = pd.read_csv("C:\\Users\\Dell\\Desktop\\TestExcel.csv")
from_df = pd.DataFrame(dframe)
Price_list = from_df['Price'].values.tolist()
Item_List = from_df['ItemName'].values.tolist()
print(Price_list)
Price_list[2] = 45
print(Price_list)

data = {'ItemName': Item_List,
        'Price':Price_list,
        'TestList':["Rishi","Mehana",0,0]}
to_df = pd.DataFrame(data,columns=['ItemName','Price','TestList'])
to_df.to_csv(r'C:\Users\Dell\Desktop\TestExcel.csv',index=False,header=True)


dframe = pd.read_csv("C:\\Users\\Dell\\Desktop\\TestExcel.csv")
from_df = pd.DataFrame(dframe)
print(from_df)


