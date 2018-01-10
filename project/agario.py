from ball import Ball
import turtle
import time
import random

#turtle.tracer()
turtle.ht()

running = True
sleep = 0.0077
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,0,0,10,"blue")
number_of_balls = 5
min_ball_r = 10
max_ball_r = 100
min_ball_dx = -5
max_ball_dx = 5
min_ball_dy = -5
max_ball_dy = 5

BALLS = []
for i in range(number_of_balls):
    ball_r = random.randint(min_ball_r,max_ball_r)
    x = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
    y = random.randint(int(-screen_height)+max_ball_r,int(screen_height)-max_ball_r)
    dx = random.randint(min_ball_dx,max_ball_dx)
    dy = random.randint(min_ball_dy,max_ball_dy)
    radius = random.randint(min_ball_r,max_ball_r)
    color = (random.random(),random.random(),random.random())
    ball = Ball(x,y,dx,dy,radius,color)
    BALLS.append(ball)
    
#def move_all_balls():
 #   for i in BALlS:
        
