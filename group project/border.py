from turtle import Turtle
import turtle
turtle.tracer(1,0)



class Border(Turtle):
    def __init__ (self,size,color,speed):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
        self.color(color)
        self.speed(speed)
        #self.tracer(tracer)


border=Border(2,'gray',10)

border.penup()
border.goto(-319,-265)
border.pendown()
turtle.hideturtle()


for i in range(2):
    for w in range(640):
        border.forward(1)
        border.stamp()
         
    border.left(90)
    for l in range(535):
        border.forward(1)
        border.stamp()
    border.left(90)

