# 윤년: 4 또는 400의 배수이면서 100의 배수가 아닌 연도
year = int(input("연도 입력: "))
if year%4 != 0 :
     print("%d년은 윤년이 아닙니다!" % year)
elif year%100 == 0 and year%400 == 0 :
     print("%d년은 윤년입니다!" % year)
elif year%100 == 0 and year%400 != 0 :
     print("%d년은 윤년이 아닙니다!" % year)
else :
     print("%d년은 윤년입니다!" % year)
