from turtle import *

def draw(x,y):
	penup()
	goto(x, y)
	pendown()

speed(5)
pensize(5)


draw(-260 , -100)
pensize(30)
left(90)
forward(200)
left(90)
forward(40)
backward(80)
draw(-260 , -100)
forward(40)
backward(80)

draw(-40 , -100)
color("red")
pensize(5)
begin_fill()
right(130)
forward(150)
circle(60 , 200)
left(225)
circle(60 , 200)
forward(150)
end_fill()

draw(180 ,100)
color("black")
pensize(30)
right(45)
forward(110)
circle(80 , 180)
forward(110)

done()