from pandas import DataFrame
student = [
    {"이름": "이강인", "국어": 73, "영어": 86, "수학": 65, "사회": 82, "과학": 86, "체육": 92 },
    {"이름": "손흥민", "국어": 93, "영어": 92, "수학": 56, "사회": 72, "과학": 88, "체육": 95 },
    {"이름": "류현진", "국어": 82, "영어": 75, "수학": 77, "사회": 86, "과학": 90, "체육": 90 },
    {"이름": "배철수", "국어": 76, "영어": 64, "수학": 82, "사회": 96, "과학": 56, "체육": 72 }
]
df = DataFrame(data=student)
print(df)
