from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle. __init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball = Ball(10,"blue",100)
ball.goto(100,0)
ball1 = Ball(50,"red",50)
ball1.goto(-100,0)
ball.backward(100)
ball1.forward(100)

balls = []
balls.append(ball)
balls.append(ball1)  

def check_collision(ball1,ball):
    xpos = ball.xcor()
    ypos = ball.ycor()
    xpos1 = ball1.xcor()
    ypos1 = ball1.ycor()
    pos = math.sqrt(math.pow(xpos-xpos1,2))
    pos1 = math.sqrt(math.pow(ypos-ypos1,2))
    if(pos == pos1):
        ball.color("black")
        ball1.color("yellow")
def teleport(ball,ball1):
    xpos = ball.xcor()
    ypos = ball.ycor()
    xpos1 = ball1.xcor()
    ypos1 = ball1.ycor()
    pos = math.sqrt(math.pow(xpos-xpos1,2))
    pos1 = math.sqrt(math.pow(ypos-ypos1,2))
    if(pos == pos1):    
        if(ball.radius > ball1.radius):
                x = random.randint(-100,100)
                y = random.randint(-100,100)
                ball.goto(x,y)
        if(ball.radius < ball1.radius):
                x = random.randint(-100,100)
                y = random.randint(-100,100)
                ball1.goto(x,y)
            
            

check_collision(ball,ball1)
teleport(ball,ball1)
