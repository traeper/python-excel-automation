import time, datetime

start_str = time.strftime("%m/%d/%Y") + " 00:00:00"
end_str = time.strftime("%m/%d/%Y ") + " 23:59:59"

print(start_str)
print(end_str)

date_1 = datetime.datetime.strptime(start_str, "%m/%d/%y")
end_date = date_1 + datetime.timedelta(days=10)

print(date_1)
print(end_date)

start_ts = int(time.mktime(time.strptime(start_str, "%m/%d/%Y %H:%M:%S")))
end_ts = int(time.mktime(time.strptime(end_str, "%m/%d/%Y %H:%M:%S")))

print(start_ts)
print(end_ts)
