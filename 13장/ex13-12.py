from datetime import * 

date1 = datetime.today()
print(date1)
cyear = date1.year
cmon = date1.month
cday = date1.day
chour = date1.hour
cmin = date1.minute
csec = date1.second
cyoil = date1.weekday()

if cyoil==0 : hyoil ="월"
elif cyoil==1 : hyoil ="화"
elif cyoil==2 : hyoil ="수"
elif cyoil==3 : hyoil ="목"
elif cyoil==4 : hyoil ="금"
elif cyoil==5 : hyoil ="토"
else : hyoil ="일"
print("현재시간 : {}년 {}월 {}일, {}시 {}분 {}초, {}요일".
      format(cyear, cmon,cday,chour,cmin,csec,hyoil))

str = date1.isoformat()
print("현재시간[ISO 형식] : ", str)
