count = 0 ;  flag = 0
while flag==0 and count<3 :
    password = input("패스워드: ")
    if password  == "Hi!python" :
        flag = 1
    else :
        print("패스워드가 틀렸습니다.")
    count = count + 1

if flag == 1 :
   print("로그-인 성공")
else :
   print("로그-인 실패")
