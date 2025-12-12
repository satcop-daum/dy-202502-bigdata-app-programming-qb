#  pip install prophet
import pandas as pd
from prophet import Prophet
from matplotlib import pyplot as plt

file_name = '../ch14/stock_005930_data.csv'
df_raw = pd.read_csv(file_name)

df_raw['ds'] = pd.to_datetime(df_raw['date'])
df_raw['y'] = df_raw['end_price']
df_raw = df_raw[df_raw['ds'].dt.year >= 2021]

print(df_raw.info())

df_data = df_raw[['ds', 'y']]

print('-'*50)
print(df_data.tail())

print('모델 객체를 생성')
model = Prophet()

print('모델을 통해서 데이터(df_data) 학습 - 시작')
model.fit(df_data)
print('모델을 통해서 데이터(df_data) 학습 - 종료')

#예측!!!(예측한 기간을 설정)
future = model.make_future_dataframe(periods=365)

print('-'*50)
print(future.tail())

#예측을 진행
forecast = model.predict(future)
print('-'*50)
print(forecast.tail())
print(forecast.info())

model.plot(forecast)
plt.show()

model.plot_components(forecast)
plt.show()
