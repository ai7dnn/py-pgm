CUTLINE = 70
name = "이강인"
middle = 76
final = 63.5
total = middle + final
avg = total / 2 
print("-----------------------------")
print("이름:", name, "\t평균:", avg)
if avg >= CUTLINE :
    print("합격! \n축하합니다.")
else :
    print("불합격! 더 노력하세요.")
    print(CUTLINE-avg, "점이 부족합니다")
print("-----------------------------")
