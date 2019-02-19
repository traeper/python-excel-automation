import pandas as pd

df_samsung = pd.read_excel('xlsx/samsung-payment.xlsx')
df_samsung.set_index('date', inplace=True)
