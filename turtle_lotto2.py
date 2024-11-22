import turtle
import random

lotto_num = []
for n in range(1,46):
    lotto_num.append(n)
#print(lotto_num)
ball_color = ["red","orange","green","blue","purple","brown"]
random.shuffle(lotto_num)
random.shuffle(ball_color)
count = 0 #볼 색깔 인덱싱 
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)

s.setup(1200,700)
s.bgcolor("black")
t.hideturtle()
t.pensize(1)
t.penup()
t.goto(0,150)
t.pendown()
t.color("white")
t.write("Random Lotto", align="center",font = ("Impact",90,"bold"))
t.penup()

for i in range(-500,501,200):
    t.penup()
    t.goto(i,-100)
    t.pendown()
    t.begin_fill()
    t.color(ball_color[count])
    t.circle(70,360)
    t.end_fill()
    #로또번호 쓰기
    t.penup()
    t.goto(i,-90)
    t.color('white')
    t.pendown()
    t.write(f"{lotto_num[count]}", align="center",font = ("Impact",90,"bold"))
    count = count + 1 




turtle.done()
