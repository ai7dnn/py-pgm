f2 = open("./result1.txt", "w")
txt = input("메시지를 남기세요.\n")
for i in range(3) :
     f2.write(txt)
     txt =  input()
f2.close()
