# TODAY CURRENT UNIX TIMESTAMP
from datetime import datetime
import calendar

utc_now = datetime.utcnow()

today = utc_now.date()

print(utc_now, today)

unixtime = calendar.timegm(utc_now.utctimetuple())
today_unixtime = calendar.timegm(today.timetuple())
print(unixtime, today_unixtime)