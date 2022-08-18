user = {'name': "키메라", 'nickname': "수선화", 'coin': 5000,  'level': "중"}
print('사용자 이름은 %s 입니다' % user['name'])
print('사용자 이름은 %s 입니다' % user.get('name'))

if user.get('이름') == None :   
      print("키 '이름'은 존재하지 않습니다. 확인 바랍니다!|\n")
print('사용자 이름은 %s 입니다'% user.get('이름'))
print('사용자 이름은 %s 입니다'% user['이름'])
