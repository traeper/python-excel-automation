#
# pandas merge
# merge by
#
import pandas as pd

df_samsung = pd.read_excel('xlsx/samsung-payment.xlsx')
df_samsung.set_index('date', inplace=True)

df_lg = pd.read_excel('xlsx/lg-payment.xlsx')
df_lg.set_index('date', inplace=True)

df_merge = pd.DataFrame()

df_merge['samsung_payment'] = df_samsung['payment']
df_merge['lg_payment'] = df_lg['payment']

print (df_merge)

path = 'sheet_column_merged.xlsx'

df_merge.to_excel(path)
