class1 = [ 70, 80, 60, 80, 90 ] 
class2 = [ 85, 95, 80, 65, 70 ]
print("class1 = ", class1) 
print("class1 = ", class1)

class1.extend(class2)
print("'class1.extend(class2)' 실행 직후 class1 = ", class1)
n = class1.count(80) 
print("class1에서 80의 개수 :", n)
class1.remove(80) 
print("'class1.remove(80)' 실행 직후 class1 ", class1)
high = max(class1) 
low = min(class1) 
print("max =", high, "min =", low)
class3 = sorted(class1)
print("'class3 = sorted(class1)' 실행 직후 class1=", class1)
print("'class3 = sorted(class1)' 실행 직후 class3=", class3)
