name = "이강인" ; eng = 66 ;  math = 83
total = eng + math ;  avg = (eng+math) / 2
print("이름:{0:s} 총점:{1:d} 평균:{2:7.2f}"  .format(name, total, avg))
print("이름:{0:s} 평균:{2:7.2f} 총점:{1:d}"  .format(name, total, avg))
print("이름:{0:s} 평균:{2:7.2f}"  .format(name, total, avg))
