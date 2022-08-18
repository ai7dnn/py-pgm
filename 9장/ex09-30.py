sum = 0 ;  i = 0
while i < 100 :
   i = i + 1
   if i % 3 == 0 :  continue
   sum = sum + i
print("합 : %d" % (sum))
