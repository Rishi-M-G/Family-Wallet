import datetime

source_datetime = datetime.datetime.now()
eod = datetime.datetime(
    year=source_datetime.year,
    month=source_datetime.month,
    day=source_datetime.day
) + datetime.timedelta(days=1, microseconds=-1)

print(eod)  # 2016-01-04 23:59:59.999999