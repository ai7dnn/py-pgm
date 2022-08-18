# def getGrade(score) : 함수 정의 생략

def getGrade(score) :
    if score>=90 :  return('A')
    elif score>=80 :  return('B')
    elif score>=70 :  return('C')
    elif score>=60 :  return('D')
    else :  return('F')

stu2 = []
n = int(input("학생 수: "))
for i in range(0, n) :
    name = input("[%d]학생 이름: " % (i))
    score1 = int(input("[%d]영어 성적: " % (i)))
    ele = dict({ "name" : name, "eng" : score1} )    # 딕셔너리 ele를 구성함
    score2 = int(input("[%d]수학 성적: " % (i)))
    ele['math']= score2    # 키가 "math"인 딕셔너리 원소 추가
    ele['total'] = score1 + score2    # 키가 "total"인 딕셔너리 원소 추가
    ele['avg'] = ele['total'] / 2    # 키가 "avg"인 딕셔너리 원소 추가
    ele['grade'] = getGrade((ele['avg']))    # 키가 "grade"인 딕셔너리 원소 추가
    stu2.append(ele)    # 리스트 stu2에 딕셔너리 ele를 추가

for i in range(0, n) :
    print(stu2[i])
