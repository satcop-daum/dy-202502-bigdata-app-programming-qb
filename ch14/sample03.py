from io import StringIO

import pandas as pd
import requests
from fontTools.ttLib.tables.E_B_L_C_ import table_E_B_L_C_

file_name = './stock_005930.csv'
df_raw = pd.read_csv(file_name)

print('-'*50)
print(df_raw.info())

rename_cols = {
    '날짜': 'date',
    '종가': 'end_price',
    '시가': 'start_price',
    '고가': 'highest_price',
    '저가': 'lowest_price'
}
drop_cols = ['전일비', '거래량']
df_raw.rename(columns=rename_cols, inplace=True)
df_raw.drop(columns=drop_cols, axis=1, inplace=True)

print('-'*50)
print(df_raw.info())
print(df_raw.head())

df_raw.set_index('date', inplace=True)
df_raw.sort_index(inplace=True)

print('-'*50)
print(df_raw.head())

df_raw.to_csv('./stock_005930_data.csv')

