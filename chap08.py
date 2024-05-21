#leg = dict()
#leg = {}

leg = {"name": '이은결', 'gender': 'female', 'height': 157, 'vision': [0.1,0.2], 'blood type': 'AB'}
#dict함수를 선언해서 딕셔너리를 만드는 경우 예약된 키워드 사용 불가, 띄어쓰기 사용 불가
#leg = dict(name='이은결', gender = 'female', height=157, vision=[0.1,0.2], bloodtype='AB')
print(leg['blood type'])
print(leg)
leg['vision'][0] = 0.3 #update
leg['python'] = 'A' #add
print(leg)


print(type(leg), type(leg['name']), type(leg['height']), type(leg['vision']))
print(f'{leg['name']}의 우측 시력은 {leg['vision'][1]}입니다.')

for k in leg:
    print(k, end = ' ')
print()
for v in leg.values():
    print(v, end = ' ')
print()
for key, value in leg.items():
    print(key, value, end = ' ') #packing -> unpacking
print()
for i in leg.items(): #packing
    print(i, end = ' ')