name = "이강인" ; eng = 66 ;  math = 83
total = eng + math ;  avg = (eng+math) / 2
print(name, total, avg)
print(format(name, "6s"), format(total, "4d"), format(avg, "6.2f"))
print("%6s %4d %6.2f" % (name, total, avg))
print("{2:6s} {1:4d} {0:6.2f}" .format(avg, total, name))
