import pandas as pd
import glob, os
import time

os.chdir('/Users/jaymac/PycharmProjects/excel_automation/lesson/lesson2/csv')
results = pd.DataFrame()

# dir_path = '/Users/jaymac/PycharmProjects/excel_automation/lesson/lesson2/csv'

for counter, file in enumerate(glob.glob("*.csv")):
    print(counter, file)
    namedf = pd.read_csv(file, skiprows=0, usecols=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    results = results.append(namedf)

# 인덱스 설정
# results.set_index('date', inplace=True)
results.to_csv('/Users/jaymac/PycharmProjects/excel_automation/lesson/lesson2/csv/result' + time.strftime("%Y%m%d") + ".csv")


from datetime import datetime, timedelta

N = 2

date_N_days_ago = datetime.now() - timedelta(days=N)

print (datetime.now())
print (date_N_days_ago)

