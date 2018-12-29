import pandas as pd

df = pd.read_excel('b.xlsx')

sorted_df = df.sort_values(by=['payment'], ascending=False)

sorted_df[0:4].to_excel('new.xlsx')
sorted_df[0:4][['payment']].to_excel('new_payment_only.xlsx')


