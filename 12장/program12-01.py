name, eng, math, total, avg, grade = [], [], [], [], [], []

infile = open("class1.txt", "r")
n = int(infile.readline().rstrip('\n'))

# n명 학생 이름, 영어 성적, 수학 성적 입력 및 리스트 name, eng, math 구성
for i in  range(0, n) :
    stu = infile.readline().rstrip('\n').split(',')
    name.append(stu[0])
    for j in range(1, len(stu)) :
        eng.append(int(stu[j]))
        math.append(int(stu[j]))
infile.close() 
