from datetime import time

t1 = time()
print(t1)
worldrecord = time(hour=2, minute=1, second=39)
korearecord = time(hour=2, minute=7, second=20)
print("마라톤 세계기록: ", worldrecord)
print("마라톤 한국기록: ", korearecord)
hourdef = korearecord.hour - worldrecord.hour
minutedef = korearecord.minute - worldrecord.minute
seconddef = korearecord.second - worldrecord.second
if seconddef < 0 :
    seconddef += 60
    minutedef -= 1
print("마라톤 기록차이:  {}시간 {}분 {}초 ".
       format(hourdef, minutedef, seconddef))
