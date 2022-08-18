import time

t1 = time.time()
print("time.time()=", t1, "\n")

str1=time.ctime(t1)
print(str1)

t2 = time.gmtime()
print(t2, "\n")

t3 = time.localtime()
print(t3)
print("현재 날짜:{}년 {}월 {}일".format(t3.tm_year,t3.tm_mon,t3.tm_mday))
print("현재 시간:{}시 {}분 {}초".format(t3.tm_hour,t3.tm_min,t3.tm_sec))
if t3.tm_wday == 0 :  wday ="월"
elif  t3.tm_wday == 1 :  wday ="화"
elif  t3.tm_wday == 2 :  wday ="수"
elif  t3.tm_wday == 3 :  wday ="목"
elif  t3.tm_wday == 4 :  wday ="금"
elif  t3.tm_wday == 5 :  wday ="토"
else :  wday ="일"
print("현재 요일: {}".format(wday))
