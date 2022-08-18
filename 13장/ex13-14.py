from datetime import date, timedelta

oneweek = timedelta(weeks=1)
print(oneweek)
sevendays =  timedelta(days=7)
print(sevendays)
fourweeks = oneweek * 4
print("4주 일수(크기):", fourweeks)
interval = fourweeks - oneweek
print("4주-1주의 일수:", interval)

current = date.today()
print("현  재 날짜 :", date.today())
after3week = current + oneweek * 3
print("3주 뒤 날짜 :", after3week)
