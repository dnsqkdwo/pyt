#기본입출력 print() input()
'''name = input("이름을 입력하세요:") #키보드로부터 값을 입력
age = input("나이는?") 
print("나의 이름은 " + name + "이고, 내 나이는 " + age + "살 입니다")'''

a = int(input("첫번째 수:")) #수5로 입력
b = int(input("두번째 수:")) #수7로 입력

print(a + b) #12
#함수는 모두 문자로 입력
#비만도 구하기 공식: 비만도 = 몸무게/(키의 제곱)*10000
# 키 height 몸무게 weight 비만도 bmi

#출력: 당신의 비만도는 000입니다 
weight = int(input('몸무게 입력:'))  #72
height = int(input('키 입력:'))  #178
BMI = weight/(height**2)*10000
print(BMI)
print("당신의 비만도는" , BMI , "입니다")











