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
    
stu = [] ;  n = int(input("학생 수: "))

for i in range(0, n) :
    name = input("[%d]학생 이름: " % (i))
    score1 = int(input("[%d]영어 성적:" % (i)))
    score2 = int(input("[%d]수학 성적:" % (i)))
    ele = [name, score1, score2, 0, 0, 0 ]
    stu.append(ele)

# 총점, 평균, 학점 계산 및 total, avg, grade 리스트 구성
for i in range(0, n) :
    stu[i][3] = stu[i][1] + stu[i][2]
    stu[i][4] = stu[i][3] / 2
    stu[i][5] = getGrade(stu[i][4])

# 전체 성적표 출력
printTitle()
for i in range(0, n) :
    printRecord(stu[i][0], stu[i][1], stu[i][2], stu[i][4], stu[i][5])

# 최고 득점자 조사 및 출력
max = 0
for i in range(1, n) :
    if stu[max][3] < stu[i][3] : max = i
print("\n최고 평균 : %6.2f(%s)" % (stu[max][4], stu[max][0]))
