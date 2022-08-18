def  getAverage(*num) :
     total = 0
     for i in num :
         total = total + i
     avg = total / len(num)
     return avg

print(getAverage(10, 20, 30))
print(getAverage(10, 20, 30, 40, 50))
print(getAverage(10, 20, 30, 40, 50, 60, 70, 80))
