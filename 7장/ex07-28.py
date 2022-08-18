n = int(input("초 시간량을 입력하세요: "))
s = n % 60  # 초 계산
m = n // 60
h = m // 60   # 시간 계산
m = m % 60   # 분 계산
print("{:d}초는 {:d}시간 {:d}분 {:d}초 입니다".format(n, h, m, s))
