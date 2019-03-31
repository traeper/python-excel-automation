import pandas as pd

df = pd.read_excel('xlsx/samsung-payment.xlsx')
# index -> column, date? no? num? ,...
# df.set_index('date', inplace=True)

# rows
print(df[df['date'].str.match('2017.1.10')])

