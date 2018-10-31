import datetime as dt


def get_now():
    return dt.datetime.now()


def get_first_of_today():
    # first seconds of today
    return get_first_of_day(get_now())


def get_last_of_today():
    # first seconds of today
    now = dt.datetime.now()
    return get_last_of_day(now)


def get_first_of_day(datetime: dt.datetime):
    # first seconds of today
    first_of_datetime = dt.datetime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=0,
        minute=0,
        second=0
    )

    return first_of_datetime


def get_last_of_day(datetime: dt.datetime):
    """
    :param datetime: 대상날짜
    :return: 대상날짜의 마지막 시간
    """
    # last seconds of today
    last_of_datetime = dt.datetime(
        year=datetime.year,
        month=datetime.month,
        day=datetime.day,
        hour=23,
        minute=59,
        second=59
    )

    return last_of_datetime


def get_day_delta_of_datetime(datetime: dt.datetime, days: int):
    """
    특정 대상 날짜에서 며칠 전, 며칠 후의 날짜를 불러오는 함수, 시분초는 영향이 없으므로 get_first_of_datetime() 함수 등을 이용해서 대상 날짜의 첫, 끝 타임스탬프를 구해야한다.
    :param datetime: 대상 날짜
    :param days: 추가 또는 뺄 날짜
    :return: 변경된 날짜
    """
    delta_datetime = datetime + dt.timedelta(days=days)
    return delta_datetime
