name = "김철수" ;  eng = 66 ;  math = 88
total = eng + math ;  avg = total / 2
print("*"*20)
print(" 이름", format(name, "^9"), sep="\t|")
print("*"*20)
print(" 영어", format(eng, "6d"), sep="\t|")
print(" 수학", format(math, "6d"), sep="\t|")
print("-"*20)
print(" 총점", format(total, "6d"), sep="\t|")
print(" 평균", format(avg, "9.2f"), sep="\t|")
print("*"*20)
