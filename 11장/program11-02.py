n = int(input("학생 수 입력 : "))
jumsu = []; ranking = []

for i in range(0, n) :
    score = int(input("[%d] 점수: " % i))
    jumsu.append(score)
    ranking.append(0)

# 석차 계산
for i in range(0, n) :
     ranking[i] = 1
     for j in range(0, n) :
          if jumsu[j] > jumsu[i] :
              ranking[i] += 1
print("-"*13)
print(" 점수\t석차")
print("-"*13)
for i in range(0, n) :
    print("  %d\t %d" % (jumsu[i], ranking[i]))
print("-"*13)
