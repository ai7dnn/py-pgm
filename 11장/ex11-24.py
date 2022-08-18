def  getBirthDay() :
     birthYear = int(input("출생연도 : "))
     birthMonth = int(input("출생월 : ")) 
     birthDate = int(input("출생일 : "))
     return birthYear, birthMonth, birthDate
  
print("학생의 생년월일을 입력하세요!")
birth = getBirthDay()
print("학생은 생년월일은 %d년 %d월 %d일 입니다!" \
      % (birth[0], birth[1], birth[2]))
