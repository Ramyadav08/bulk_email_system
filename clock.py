from turtle import *
import time
time.time()
t=Turtle()
wn=Screen()
wn.title("my simple clock")
wn.bgcolor("black")
wn.setup(600,600)
t.speed(3)
t.pensize(3)
t.hideturtle()
wn.tracer(0)
def draw_clock(h,m,s,t):
    t.penup()
    t.goto(0,210)
    t.setheading(180)
    t.pencolor("green")
    t.pendown()
    t.circle(210)
    #to centre
    t.penup()
    t.goto(0,0)
    t.setheading(90)
    # for hours
    for i in range(12):
        t.forward(180)
        t.pendown()
        t.fd(30)
        t.penup()
        t.goto(0,0)
        t.right(30)
    t.penup()
    t.goto(0, 0)
    t.setheading(90)
    # for minute
    for i in range(60):
        t.forward(200)
        t.pendown()
        t.fd(10)
        t.penup()
        t.goto(0, 0)
        t.right(6)
    #hour hand
    t.penup()
    t.goto(0,0)
    t.pencolor("red")
    t.setheading(90)
    angle=(h/12)*360
    t.right(angle)
    t.pendown()
    t.fd(80)
    # to minute
    t.penup()
    t.goto(0, 0)
    t.pencolor("green")
    t.setheading(90)
    angle = (m / 60) * 360
    t.right(angle)
    t.pendown()
    t.fd(130)
    #to second
    t.penup()
    t.goto(0, 0)
    t.pencolor("yellow")
    t.setheading(90)
    angle = (s / 60) * 360
    t.right(angle)
    t.pendown()
    t.fd(150)

while True:
    h=int(time.strftime("%I"))
    m= int(time.strftime("%M"))
    s= int(time.strftime("%S"))
    draw_clock(h,m,s,t)
    wn.update()
    time.sleep(1)
    t.clear()
mainloop()