# 학점 판정 함수(getGrade(score)) 생략으로 실행 시 오류 발생
name, eng, math, total, avg, grade = [], [], [], [], [], [] 

def readData() :
    global name, eng, math
    name=input("이름: ") ; eng=int(input("영어 성적: ")) ; math=int(input("수학 성적: "))

def getAvg(eng, math, n) :
    return((eng+math) / n)

def getGrade(score) :
    if score>=90 :  return('A')
    elif score>=80 :  return('B')
    elif score>=70 :  return('C')
    elif score>=60 :  return('D')
    else :  return('F')

def printTitle() :
    print("-"*53)
    print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
    print("-"*53)

def printRecord(name, subj1, subj2, mean, level) :
    print(" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name, subj1,subj2, \
           subj1+subj2, mean, level))
    print("-"*53)

def processOne() :
    global avg, grade
    readData()
    avg = getAvg(eng, math, 2)
    grade = getGrade(avg)
    printTitle()
    printRecord(name, eng, math, avg, grade)
    
n = int(input("학생 수 입력 : "))
# n명 학생 이름, 영어, 수학 성적 입력 및 리스트 name, eng, math 구성
for i in  range(0, n) :
    print("\n%d번째 학생 자료 입력" % i)
    name.append(input("이름: "))
    eng.append(int(input("영어 성적: ")))
    math.append(int(input("수학 성적: ")))

# 총점, 평균, 학점 계산 및 total, avg, grade 리스트 구성
for i in range(0, n) :
    total.append(eng[i] + math[i])
    avg.append(total[i] / 2)
    grade.append(getGrade(avg[i]))

# 전체 성적표 출력
printTitle()
for i in range(0, n) :
    printRecord(name[i], eng[i], math[i], avg[i], grade[i])

# 최고 득점자 조사 및 출력
max = 0
for i in range(1, n) :
    if total[max] < total[i] : max = i
print("\n최고 평균 : %6.2f(%s)" % (avg[max], name[max]))
