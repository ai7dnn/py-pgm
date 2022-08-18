n = int(input("양의 정수: "))
flag = 0
for i in range(2, n) :
    if n%i == 0 :
        flag = 1
        break
if flag==0 :
    print("%d은 소수임" % (n))
else :
    print("%d은 소수가 아님" % (n))
