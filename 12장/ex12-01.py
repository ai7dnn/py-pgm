n= int(input("학생 수는 ? "))
print(n, "학생들(%d)의 성적을 순차적으로 입력하세요")

student = [ ]
for i in range(0, n) :
    score = int(input())
    student.append(score)

print("입력 데이터 :", student)
student.sort()
print("정렬 데이터 :", student)
