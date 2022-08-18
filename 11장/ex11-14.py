# 학점 판정 함수(getGrade(score)) 생략으로 실행 시 오류 발생
score = [88, 75, 92, 64, 82]
total=0
for jumsu in score :
    total = total + jumsu
    grade = getGrade(jumsu)
    print("%3d : %2s" % (jumsu, grade))
avg = total / len(score)
print("\n 리스트 평균 :", avg)
