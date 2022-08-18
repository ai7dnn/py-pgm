from pandas import Series
student1 = [ 93, 92, 56, 72, 88, 95 ]
student2 = [ 73, 86, 65, 82, 86, 92 ]
s1 = Series(data=student1)
s2 = Series(data=student2)
print(s1+s2, end="\n\n")   # ①
print(s1*2, end="\n\n")   # ②
print(s1-s2)   # ③
