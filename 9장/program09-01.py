n = int(input("학생 수 입력 : "))
count = cTotal = 0

while count < n :
    print(" \n%d번째 학생 성적 처리" % count)

    name = input("이름: ")
    eng = int(input("영어 성적: ")) ;  math = int(input("수학 성적: "))
    total = eng + math ;  avg = total / 2

    # 학점 판정
    if avg>=90 :  grade = 'A'
    elif avg>=80 :  grade = 'B'
    elif avg>=70 :  grade = 'C'
    elif avg>=60 :  grade = 'D'
    else :  grade =  'F'

    # 결과 출력
    print("-"*53)
    print(" 이  름\t\t영어\t수학\t총점\t평균\t학점")
    print("-"*53)
    print (" %s\t\t%3d\t%3d\t%3d\t%.2f\t%2c" % (name, eng, math, total, avg, grade))
    print("-"*53)

    cTotal += total
    count += 1

cAvg = cTotal/(2*n)
print(" \n학생 수 : %d, 전체 평균 : %6.2f\n" % (n, cAvg))
