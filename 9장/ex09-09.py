months = int(input("월의 날짜 수(1-31) ? : "))
startDay = int(input("월의 첫 번째 요일(일:0 - 토:6) ? : "))

# 달력의 요일 출력
print("\n--------------------")
print("일 월 화 수 목 금 토")

# 첫 번째 주의 1일 이전 요일(빈칸) 출력
i = 0
while i < startDay :
    print('  ', end=' ')
    i = i + 1

# 1~months까지의 날짜 출력
n = 1

day = startDay
while n <= months :
    if day % 7  == 0:
       day = 0
       print('\n', end='')

    print("%2d" % (n), end=' ')
    day = day + 1
    n = n + 1
print("\n--------------------")
