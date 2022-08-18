from pandas import Series
student1 = ["손흥민", 93, 92, 56, 72, 88, 95 ]
index1 = ["이름", "국어", "영어", "수학", "사회", "과학", "체육"]
s = Series(data=student1, index=index1)
print(s) 
