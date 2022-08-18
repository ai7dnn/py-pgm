from datetime import date, timedelta

now = date.today()
oneDay = timedelta(days=1)
tomorrow = now + oneDay
yesterday = now - oneDay
print("어제:", yesterday)
print("오늘:", now)
print("내일:", tomorrow)
