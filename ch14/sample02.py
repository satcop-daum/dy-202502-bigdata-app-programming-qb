from io import StringIO

import pandas as pd
import requests
from fontTools.ttLib.tables.E_B_L_C_ import table_E_B_L_C_

# 1 - 737

request_header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
}

all_table_data = pd.DataFrame()

total_page = 737
for index in range(1, total_page + 1):
    print('-'*50)
    print(f'{index}/{total_page}')

    url = f'https://finance.naver.com/item/sise_day.naver?code=005930&page={index}'
    response = requests.get(url, headers=request_header)

    print(response.status_code)
    # print(response.text)
    raw_data = response.text

    dy_data = pd.read_html(StringIO(raw_data))
    table_data = dy_data[0]

    # print(table_data.info())
    print(table_data.head())

    all_table_data = pd.concat([all_table_data, table_data])
#for-end

all_table_data.dropna(inplace=True)

print('-'*50)
print(all_table_data.info())
print(all_table_data.head())

all_table_data.to_csv('./stock_005930.csv', index=False)




