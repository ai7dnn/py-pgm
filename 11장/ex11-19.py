class1 = [
          [88, 75, 96, 74, 82],
          [72, 82, 63, 88, 76],
          [92, 84, 82, 96, 76]
         ]
classSum=0 ; i=0;  numSubj=0
for stu in class1:
    sum = 0
    for subj in stu :
        sum = sum + subj
    avg = sum / len(stu)
    print ("%d번 학생 : 총점=%d, 평균=%6.2f" % (i, sum, avg))
    i = i + 1
    numSubj += len(stu)
    classSum = classSum + sum
avgClass = classSum / (numSubj)
print("전체 평균 = %6.2f" % (avgClass))
