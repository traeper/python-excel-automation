import time, datetime

start_str = time.strftime("%m/%d/%Y") + " 00:00:00"
end_str = time.strftime("%m/%d/%Y ") + " 23:59:59"

print(start_str)
print(end_str)

start_ts = int(time.mktime(time.strptime(start_str, "%m/%d/%Y %H:%M:%S")))
end_ts = int(time.mktime(time.strptime(end_str, "%m/%d/%Y %H:%M:%S")))

print(start_ts)
print(end_ts)
