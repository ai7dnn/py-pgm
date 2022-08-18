name = "이강인" ; eng = 66 ;  math = 83
total = eng + math ;  avg = (eng+math) / 2

print("이름:{0:s} 평균:{2:7.3f} 총점:{1:d} ".format(name, total, avg))
print("이름:{0:s} 총점:{1:d}\n이름:{0:s} 평균:{2:7.3f}".format(name, total, avg))
print("평균:{2:6.2f} 평균:{2:8.4f}".format(name, total, avg))
