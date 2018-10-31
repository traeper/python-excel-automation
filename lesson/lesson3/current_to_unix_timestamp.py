# TODAY CURRENT UNIX TIMESTAMP
from util import date_util as du

# 오늘의 첫 시각
first_of_today = du.get_first_of_today()
print("[FIRST_OF_TODAY] datetime : ", first_of_today, "unix timestamp",  int(first_of_today.timestamp()))


# 오늘의 마지막 시각
last_of_today = du.get_last_of_today()
print("[LAST_OF_TODAY] datetime : ", last_of_today, "unix timestamp",  int(last_of_today.timestamp()))


# 현재로부터 10일 전, 그 날의 첫 시각
now = du.get_now()
before_10_days = du.get_day_delta_of_datetime(now, -10)
first_of_before_10_days = du.get_first_of_day(before_10_days)
print("[FIRST_OF_BEFORE_10_DAYS] datetime : ", first_of_before_10_days, "unix timestamp",  int(first_of_before_10_days.timestamp()))


# 현재로부터 10일 후, 그 날의 마지막 시각
now = du.get_now()
after_10_days = du.get_day_delta_of_datetime(now, 10)
last_of_after_10_days = du.get_last_of_day(after_10_days)
print("[LAST_OF_AFTER_10_DAYS] datetime : ", last_of_after_10_days, "unix timestamp",  int(last_of_after_10_days.timestamp()))


