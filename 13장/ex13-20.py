from pandas import DataFrame
student = [
    ["이강인", 73, 86, 65, 82, 86, 92 ],
    ["손흥민", 93, 92, 56, 72, 88, 95 ],
    ["류현진", 82, 75, 77, 86, 90, 90 ],
    ["배철수", 76, 64, 82, 96, 56, 72 ]
]
columns = ["이름", "국어", "영어","수학", "사회", "과학", "체육"]
df = DataFrame(data=student, columns=columns)
print(df) 
