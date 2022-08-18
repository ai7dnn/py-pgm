score1 = int(input("1차 성적 : "))
score2 = int(input("2차 성적 : "))
total = score1 + score2
avg = total / 2
if avg > 90 :   
    level = "매우 우수"
if 70 <= avg < 90 :   
    level = "우수"
if 60 <= avg < 70 :   
    level = "보통"
if avg < 60 :   
    level = "미흡"
print ("평균 :", avg, "(", level, ")")
