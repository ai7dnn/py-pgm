sum= 0
for i in range(1, 1000) :
    sum = sum+i
    if  sum>1000 :
         break
print("누적 합이 1000을 넘을 때 :", sum)
print("누적 합이 1000을 넘을 때의 정수:", i)
