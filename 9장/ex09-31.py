sum = 0
for  i  in range(1, 1001) :
    if  i%7 == 0 : continue
    sum = sum + i
    if  sum>1000 : break

print("처음으로 1000을 넘을 때의 합 : %d " % sum)
print("마지막에 더해진 정수 : %d " % i)
