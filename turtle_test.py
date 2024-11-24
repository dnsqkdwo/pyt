import turtle

turtle.shape('turtle')

#삼각형 그리기
'''
for t in range(3):
    turtle.forward(100)
    turtle.left(120)


n = int(input('몇각형을 그릴까요?:'))

for i in range(n):
    turtle.forward(100)
    turtle.left(360/n)
'''

#8각형부터 삼각형까지 순서대로 그리기

turtle_color= ['red','orange','yellow','green','blue','purple']
n = int(input('몇각형을 그릴까요?:'))

for n in range(8,2,-1):# i값 8 7 6 5 4 3
    turtle,color(turtle_color[8-n])
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(100)
        turtle.left(360/n)
    turtle.end_fill()
