infoHobby = { '바둑': 5 , '독서' : 5, '영화감상': 5 }
print("통계 조사 전 : ", infoHobby, end="\n\n")
for i in range(5) :
    print("학생들의 여가 활동에 대한 통계 조사 중입니다")
    hobby = input("학생의 여가 활동은 무엇입니까? ")
    if hobby in infoHobby.keys():
        infoHobby[hobby] += 1
    else :
        infoHobby[hobby] = 1
print("\n5명 통계 조사 후 : ", infoHobby)
