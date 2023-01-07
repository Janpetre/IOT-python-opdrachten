import turtle

turtle.setup (width=500, height=500, startx=0, starty=-1)

t = turtle.Turtle()

t.setheading(90)
for i in range (5):
    t.fd(10)
    t.lt(90)
    t.fd(20)
    t.bk(20)
    t.rt(90)
    for i in range (4):
        t.fd(10)
        t.lt(90)
        t.fd(10)
        t.bk(10)
        t.rt(90)

turtle.done()