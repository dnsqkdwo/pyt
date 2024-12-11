#사용자 정의 함수
#1. 인수 매개변수
'''
def hello(age=17,name='김인평',job='ㅎ'):
    print('안녕하세요')
    print(f'{name}입니다')
    print(f'제 나이는 {age}세입니다')
    print(f'제 직업은 {job}입니다')  

hello(job='프로그래머')
#hello('아이유',31,'가수')
#hello('방시혁',52,'교주')

#2. return
#두 수의 합을 구하는 함수

def add_num(num1,num2):
    print(f'{num1}와 {num2}을 입력받았습니다.')
    hap = num1 + num2
    return(hap)

hap = add_num(15,7)
print(f'두 수의 합은 {hap}입니다.')

'''

#리스트 score에 있는 학생 성적을 넘겨 받아 총점, 평균, 최고점수, 최저점수를 리턴하는 함수 작성

def scoreFunc(scoreList):
    total = sum(scoreList)
    avg = total/len(scoreList)
    max_score = max(scoreList)
    min_score = min(scoreList)
    return total, avg, max_score, min_score

score = [90,80,10,50,95]
total, avg, max_score, min_score = scoreFunc(score)
print('총점: ', total)
print('평균: ', avg)
print('최고점수: ', max_score)
print('최저점수: ', min_score)





