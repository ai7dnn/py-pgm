user = {'name': "키메라", 'nickname': "수선화", 'coin': 5000,  'level': "중"}
print("user.keys()의 출력 결과 : ", user.keys())
print("딕셔너리 user의 키 리스트 : ", list(user.keys()))
print("user.values()의 출력 결과 : ", user.values())
print("user.items()의 출력 결과 : ", user.items())

# .keys() 함수의 활용
if 'income' in user.keys() :
    user['income'] =  user['income'] + user['coin']
    user['coin'] = 0
else :
    user['income'] =  user['coin']
    user['coin'] = 0
print("user['coin']=",user['coin'], "user['income']=", user['income'])

user['coin']= 500
if 'income' in user.keys() :
    user['income'] =  user['income'] + user['coin']
    user['coin'] = 0
else :
    user['income'] =  user['coin']
    user['coin'] = 0
print("user['coin']=",user['coin'], "user['income']=", user['income'])
