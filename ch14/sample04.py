from matplotlib import pyplot as plt
import pandas as pd

file_name = './stock_005930_data.csv'
df_raw = pd.read_csv(file_name)

lowest_price = 5
highest_price = 11

df_raw['date_time'] = pd.to_datetime(df_raw['date'])
df_raw = df_raw[df_raw['date_time'].dt.year >= 2021]
df_raw.drop(columns=['date_time'], axis=1, inplace=True)

# 5,6,7,8,9,10,11
# 8 = 11 - ((11 - 5) / 2)
# 11 - 3
# 8
# middle_price = highest_price - ((highest_price - lowest_price) / 2)
df_raw['middle_price'] = df_raw['highest_price'] - ((df_raw['highest_price'] - df_raw['lowest_price']) / 2)

df_raw['date_month'] = df_raw['date'].str[0:7]
df_raw.set_index('date', inplace=True)


print('-'*50)
print(df_raw.info())
print(df_raw.head())

df_raw.plot.line()
plt.show()

#df_raw[-50:].boxplot(column='middle_price', by=['date_month'])
#plt.show()




