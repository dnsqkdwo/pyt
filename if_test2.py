#제어문 - 조건문

#홀짝 판별

#수하나 입력
#입력된 수가 홀수 or 짝수인지 판별

'''
n = int(input('정수하나를 입력하세요:'))
if n %2 == 1: #홀수
    print(f'{n}은 홀수입니다')
else:
    print(f'{n}은 짝수입니다')

#합격 탈락 판별 
score = int(input('점수를 입력하세요:'))
if score >= 60:
    print('합격')
else:
    print('불합격')
    '''

#열날때 행동 요령

temp = int(input('체온을 입력하세요:'))
if temp >= 40:
           print('당장 응급실로 가세요')
elif temp >= 38:
    print('병원을 가세요')
elif 37 >= temp >= 36:
    print('학교에 가서 보건선생님을 만나요')
else:
    print('정상입니다 학교로 가세요')

#학점 판별
score = int(input('점수를 입력하세요:'))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('c')
elif score >= 60:
    print('D')
else:
    print('E')

    






















