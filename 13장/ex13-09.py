from random import *

seed()
print("주사위 던지기 결과 : ", randrange(6)+1)
print("0~20 사이의 임의의 3의 배수 생성하기 : ", randrange(0, 20, 3))
print("1~46 사이의 행운번호 생성하기 : ", randint(0, 46))
days = ['일', '월', '화', '수', '목', '금', '토']

print("임의의 요일 선택하기 : ", choice(days))
print("임의의 요일을 2회 선택하기 : ", choices(days, k=2))
print("임의의 요일을 2회 선택하기 : ", choices(days, [10,10,10,10,60,80,80],k=2))

vocations = sample(days, k=3)
print("임의 휴식 요일 : ", vocations)

print("요일 순서 임의로 섞기 전 : ", days)
shuffle(days) 
print("요일 순서 임의로 섞기 후 : ", days)

a=random()
b=uniform(0, 100)
print("random()= {}, uniform(0, 100)={} ".format(a, b))
