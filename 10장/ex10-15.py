def gcd(n1, n2) :
    if  n2 == 0 : return n1
    else : return gcd(n2, n1%n2)

x = int(input("정수1: "))
y = int(input("정수2: "))
if  x<y :
    temp = x ; x = y ; y = temp
print("%d, %d의 최대공약수 : %d" % (x,y,gcd(x,y)))
