# 학점 판정 함수(getGrade(score)) 생략으로 실행 시 오류 발생
score = [88, 75, 92, 64, 82]
n = len(score)
total = 0
for i in range(n) :
    total = total + score[i]
    grade = getGrade(score[i])
    print("%3d : %2s" % (score[i], grade))
avg = total / n
print("\n 리스트 평균 :", avg)
