# 학점 판정 함수(getGrade(score)) 생략으로 실행 시 오류 발생
name = ["차범근", "이강인", "손흥민", "이동국", "박지성"]
score = [88, 75, 92, 64, 82]
n = len(name)
total=0
for i in range(n) :
    total = total + score[i]
    grade = getGrade(score[i])
    print("%3s : %3d : %3s" % (name[i], score[i], grade))
avg = total / n
print("\n학생 수 :", n)
print("학생 평균 :", avg)
