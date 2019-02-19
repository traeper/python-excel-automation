#
# Example) merge one sheet
#

import pandas as pd

df = pd.read_excel('b.xlsx')

print("before sorting")
print(df)

print("\nafter sorting")
sorted_df = df.sort_values(by=['payment'], ascending=False)
print(sorted_df)

print("\nslicing sorted data frame")
print(sorted_df[0:4])

print("\nsummation payments")
print(sorted_df[0:4]['payment'].sum())


