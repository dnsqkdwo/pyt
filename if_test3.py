'''
money = int(input('가지고 있는 돈은 얼마인가요?'))
#7000입력
if money >= 20000:  #실행 => False
    print('탕수육')
elif money >= 10000:  #실행 => False
    print('쟁반짜장')
elif money >= 6000:   #실행 =>True
    print('해물 짬뽕')
elif money >= 4000: #X
    print('짜장면')
else:
    print('단무지 먹자')#X


list_num = [1,2,3,4,5]

n = int(input('정수하나 입력하세요:'))

if n in list_num:
    print(f'{n}은 목록 안에 있습니다')
else:
    print(f'{n}은 찾을 수 없습니다')
'''




a = int(input('첫번째 주사위의 값'))
b = int(input('첫번째 주사위의 값'))


if a%2 ==1 and b%2 ==1:
    print(a**2+b**2)
elif a%2==0 and b%2==0:
    print(abs(a-b))
else:
    print(2*(a+b))

    
