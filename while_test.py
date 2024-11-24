#while 반복문 
#1~100까지 출력
'''
for i in range(1,101):
    print(i)

i = 1
while i <= 100: 
    print(i)
    i += 1 # i = i+1


#3~5출력하는 while문 
i = 3
while i <= 5: 
    print(i)
    i += 1
    

#'파이썬 최고!!'문장을 13출력 while
i = 1
while i <= 13: 
    print(f'{i}.파이썬 최고!!')
    i += 1 


i = 1
while i <=100:
    if i % 10 == 0:
        print(i) #다음줄로 넘기지 않고 출력
    else:
        print(i, end=' ') #10단위마다 다음줄로 넘긴다
        
    i += 1
  


#두개의 정수를 입력받아 더하여 출력하는 프로그램  
#(첫번째 값 두번째 값)
#두 값 모두 0이 입력되었을 때 종료 하도록 하세요 break
while True:
    print('두개의 정수값을 입력하세요')
    num1 = int(input('첫번째 정수 값: '))
    num2 = int(input('두번째 정수 값: '))
    print(f'두 수의 합은 {num1+num2}입니다')
    if num1==0 and num2 == 0:
        break #무한 반복문 탈출조건

x = 3
while x < 6:
    print(x)
    x += 1


echo = input()
while echo !='exit':
    print(echo)
    echo = input()

echo = input()
while True:
    if echo == 'exit':
        break
    print(echo)
    echo = input()
'''