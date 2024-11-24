#반복문
#1. 문자열
#2. 리스트 변수
#3. range()함수를 활용한 반복
'''
sum_number = 0
for i in range(1,101,1):
    sum_number = sum_number + i
print(f'1~100까지의 합: {sum_number}')

#구구단 구하기
#3단 출력  
for i in range(1,10):
    print(f'3*{i} =  {3*i}')
'''
#중복 for문
for i in range(2,10):
    print(f'\n{i}단')
    for j in range(1,10):
        print(f'{i}*{j} =  {i*j}')
