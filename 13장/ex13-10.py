from datetime import date

date1 = date.today()
print("date1=", date1)
print("오늘은 {}년 {}월 {}일 입니다.".\
      format(date1.year, date1.month, date1.day))

day1 = date1.weekday()
if day1==0 : hday ="월"
elif day1==1 : hday ="화"
elif day1==2 : hday ="수"
elif day1==3 : hday ="목"
elif day1==4 : hday ="금"
elif day1==5 : hday ="토"
else : hday ="일"
print("오늘은 {}요일 입니다.".format(hday))

date2 = date1.replace(month=11, day=22)
print("올해 수능일: {}".format(date2.isoformat()))
