import turtle
flag = turtle.Turtle()

flag.speed(5)
flag.pensize(5)
flag.color("blue")

def draw(x,y):
	flag.penup()
	flag.goto(x, y)
	flag.pendown()

for i in range(24):
    flag.forward(80)
    flag.backward(80)
    flag.left(15)	

draw(0 , -80)    

flag.circle(80)

draw(-350 , -100)
flag.color("green")
flag.begin_fill()
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.end_fill()

draw(350 , 100)
flag.color("orange")
flag.begin_fill()
flag.right(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.left(90)
flag.forward(200)
flag.left(90)
flag.forward(700)
flag.end_fill()




turtle.done()