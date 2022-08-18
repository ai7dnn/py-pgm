from pandas import DataFrame
student = [
    ["이강인", 73, 86, 65, 82, 86, 92, 0, 0, '' ],
    ["손흥민", 93, 92, 56, 72, 88, 95, 0, 0, '' ],
    ["류현진", 82, 75, 77, 86, 90, 90, 0, 0, '' ],
    ["배철수", 76, 64, 82, 96, 56, 72, 0, 0, '' ]
]
columns = ["이름", "국어", "영어","수학", "사회", "과학", "체육", "총점", "평균", "평균" ]
stu = DataFrame(data=student, columns=columns)

print("[1] 데이터프레임 생성 결과")
print(stu)
print("\n-------------------------------------------")
print("[2] 데이터프레임 처리 결과")
i = 0
while i < 4 :
   stu.iloc[i, 7] = stu.iloc[i,1] + stu.iloc[i, 2] + stu.iloc[i, 3] + stu.iloc[i, 4] + stu.iloc[i, 5] + stu.iloc[i, 6]
   stu.iloc[i, 8] = stu.iloc[i, 7] / 6.0
   if stu.iloc[i, 8]>= 90:  stu.iloc[i, 9] = 'A'
   elif stu.iloc[i, 8]>= 80:  stu.iloc[i, 9] = 'B'
   elif stu.iloc[i, 8]>= 70:  stu.iloc[i, 9] = 'C'
   elif stu.iloc[i, 8]>= 60:  stu.iloc[i, 9] = 'D'
   else:  stu.iloc[i, 8]= 'F'
   i += 1
print(stu)
stu.to_csv('./pandas1.csv', encoding='euc-kr')
stu.to_excel('./pandas2.xlsx', encoding='euc-kr')
