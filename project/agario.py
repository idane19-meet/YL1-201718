from ball import Ball
import turtle
import time
import random
import math

#turtle.tracer()
turtle.ht()

RUNNING = True
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
    x = random.randint(int(-screen_height)+max_ball_r,int(screen_height)-max_ball_r)
    y = random.randint(int(-screen_height)+max_ball_r,int(screen_height)-max_ball_r)
    dx = random.randint(min_ball_dx,max_ball_dx)
    dy = random.randint(min_ball_dy,max_ball_dy)
    radius = random.randint(min_ball_r,max_ball_r)
    color = (random.random(),random.random(),random.random())
    ball = Ball(x,y,dx,dy,radius,color)
    BALLS.append(ball)
    
def move_all_balls():
    for i in BALLS:
        i.move(screen_width,screen_height)
        
def collide(ball_a,ball_b):
    d = math.sqrt(math.pow(ball_a.x-ball_b.x,2) + math.pow(ball_a.y-ball_b.y,2))
    if ball_a.r == ball_b.r and ball_a.x == ball_b.x and ball_a.y == ball_b.y:
        return False
    if d+10 <= ball_a.r + ball_b.r:
       return True
    else:
        return False

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            check = collide(ball_a,ball_b)
            if(check):
                a =  ball_a.r
                b = ball_b.r
                if a > b:
                    ball_b.x = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.y = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.r = random.randint(min_ball_r,max_ball_r)
                    ball_b.color = (random.random(),random.random(),random.random())
                    while ball_b.dx <= 0 or ball_b.dy <= 0:
                        dx = random.randint(min_ball_dx,max_ball_dx)
                        dy = random.randint(min_ball_dx,max_ball_dx)
                    ball_a.r+=1
                    ball_a.shapesize(ball_a.r)
                    ball_b.shapesize(ball_b.r)
                elif a < b:
                    ball_a.x = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_a.y = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_a.r = random.randint(min_ball_r,max_ball_r)
                    ball_a.color = (random.random(),random.random(),random.random())
                    while ball_a.dx <= 0 or ball_a.dy <= 0:
                        dx = random.randint(min_ball_dx,max_ball_dx)
                        dy = random.randint(min_ball_dx,max_ball_dx)
                    ball_b.r+=1
                    ball_a.shapesize(ball_a.r)
                    ball_b.shapesize(ball_b.r)
def check_myball_collision(MY_BALL):
    for ball_b in BALLS:
        check1 = collide(MY_BALL,ball_b)
        if(check1):
            a = MY_BALL.r
            b = ball_b.r
            if(a < b):
                    MY_BALL = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    MY_BALL.y = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    MY_BALL.r = random.randint(min_ball_r,max_ball_r)
                    MY_BALL.color = (random.random(),random.random(),random.random())
                    while MY_BALL.dx <= 0 or MY_BALL.dy <= 0:
                        dx = random.randint(min_ball_dx,max_ball_dx)
                        dy = random.randint(min_ball_dx,max_ball_dx)
                    ball_b.r+=1
                    MY_BALL.shapesize(ball_a.r)
                    ball_b.shapesize(ball_b.r)
            elif(a > b):
                    ball_b.x = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.y = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.r = random.randint(min_ball_r,max_ball_r)
                    ball_b.color = (random.random(),random.random(),random.random())
                    while ball_b.dx <= 0 or ball_b.dy <= 0:
                        dx = random.randint(min_ball_dx,max_ball_dx)
                        dy = random.randint(min_ball_dx,max_ball_dx)
                    MY_BALL.r+=1
                    MY_BALL.shapesize(ball_a.r)
                    ball_b.shapesize(ball_b.r)
    return True
def Movearound(event):
    MY_BALL.x = event.x-screen_width
    MY_BALL.y = event.y-screen_height



while(RUNNING):
    if screen_width == turtle.getcanvas().winfo_width()/2 and screen_height == turtle.getcanvas().winfo_height()/2:
        move_all_balls()
        check_all_balls_collision()
        MY_BALL.move(screen_width,screen_height)
        print(MY_BALL)
        in_game = check_myball_collision(MY_BALL)
    else:
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2
    turtle.update()
    

    
