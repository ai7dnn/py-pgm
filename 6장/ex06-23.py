solar = ['수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
star = "지구"
if star in solar :   # 변수 star 값이 리스트 solar에 있다면
    print ("우리는 태양계에 살고 있습니다.")
print("우리가 사는 별 : ", solar[2])
solar[2] =  '푸른별-지구'
print(solar[2])
