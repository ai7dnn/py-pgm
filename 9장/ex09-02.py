print("-1을 입력할 때까지 입력되는 정수의 합 구하기")
num = int(input("정수 입력 : "))
sum = 0
while num != -1 :
    sum = sum + num
    num = int(input("정수 입력 : "))

print("입력된 정수의 합 : ", sum)
