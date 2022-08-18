name=eng=math=topAvg=topName=None
    
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

print("\n프로그램 시작")
n = int(input("학생 수 입력 : "))

# 첫 번째 학생 성적 처리
print("\n%d번째 학생 성적 처리" % 0)
processOne() ; topAvg = avg ;  topName = name

# 두 번째~n번째 학생 성적 처리
for i in range(1, n) :
    print("\n%d번째 학생 성적 처리" % i)
    processOne()
    if topAvg < avg :
        topAvg = avg ; topName = name
        
print("\n최고 평균 : %6.2f(%s)" % (topAvg,topName))
print("\n프로그램 종료")
