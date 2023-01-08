import turtle

turtle.setup (width=500, height=500, startx=0, starty=-1)
scrn = turtle.Screen()
t = turtle.Turtle()

for i in range (5):
    t.fd(10)
    t.rt(90)
    t.fd(20)
    t.bk(20)
    t.lt(90)
    for i in range (5):
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.backward(10)
        t.left(90)

turtle.done()