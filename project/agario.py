from ball import Ball
import turtle
import time
import random
import math

turtle.tracer(0)
turtle.ht()
turtle.bgpic("a.gif")
RUNNING = True
sleep = 0.0077
screen_width = turtle.getcanvas().winfo_width()
screen_height = turtle.getcanvas().winfo_height()
##turtle.screensize(1000,1000)
turtle.setup(1280,1025)
MY_BALL = Ball(0,0,0,0,40,"white")
turtle.pencolor("white")
turtle.write("radius is: " + str(MY_BALL.r),move=False,align = "center",font=("Arial", 40, "normal"))
number_of_balls = 10
min_ball_r = MY_BALL.r-10
max_ball_r = MY_BALL.r+10
min_ball_dx = -5
max_ball_dx = 5
min_ball_dy = -5
max_ball_dy = 5

BALLS = []
for i in range(number_of_balls):
    ball_r = random.randint(min_ball_r,max_ball_r)
    x = random.randint(int(-screen_height)+max_ball_r,int(screen_height)-max_ball_r)
    y = random.randint(int(-screen_height)+max_ball_r,int(screen_height)-max_ball_r)
    while MY_BALL.x == x and MY_BALL.y == y:
        x = random.randint(int(-screen_height)+max_ball_r,int(screen_height)-max_ball_r)
        y = random.randint(int(-screen_height)+max_ball_r,int(screen_height)-max_ball_r)
    dx = random.randint(min_ball_dx,max_ball_dx)
    dy = random.randint(min_ball_dy,max_ball_dy)
    while dx == 0 or dy == 0:
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
    d = math.sqrt(math.pow(ball_a.xcor()-ball_b.xcor(),2) + math.pow(ball_a.ycor()-ball_b.ycor(),2))
    if ball_a == ball_b:
        return False
    if d+10 <= ball_a.r + ball_b.r:
       return True
    else:
        return False

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            check = collide(ball_a,ball_b)
            if check:
                a =  ball_a.r
                b = ball_b.r
                if a > b:
                    ball_b.x = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.y = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.goto(ball_b.x, ball_b.y)
                    ball_b.r = random.randint(min_ball_r,max_ball_r)
                    ball_b.color = (random.random(),random.random(),random.random())
                    dx = random.randint(min_ball_dx+6,max_ball_dx)
                    dy = random.randint(min_ball_dx+6,max_ball_dx)
                    while dx == 0 or dy == 0:
                        dx = random.randint(min_ball_dx+6,max_ball_dx)
                        dy = random.randint(min_ball_dx+6,max_ball_dx)
                    ball_b.dx = dx
                    ball_b.dy = dy
                    ball_a.r+=5
                    ball_a.shapesize(ball_a.r/10)
                    ball_b.shapesize(ball_b.r/10)
                elif a < b:
                    ball_a.x = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_a.y = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_a.goto(ball_a.x, ball_a.y)
                    ball_a.r = random.randint(min_ball_r,max_ball_r)
                    ball_a.color = (random.random(),random.random(),random.random())
                    dx = random.randint(min_ball_dx+6,max_ball_dx)
                    dy = random.randint(min_ball_dx+6,max_ball_dx)
                    while dx == 0 or dy == 0:
                        dx = random.randint(min_ball_dx+6,max_ball_dx)
                        dy = random.randint(min_ball_dx+6,max_ball_dx)
                    ball_a.dx = dx
                    ball_a.dy = dy
                    ball_b.r+=5
                    ball_a.shapesize(ball_a.r/10)
                    ball_b.shapesize(ball_b.r/10)
##thor = turtle.clone()
def check_myball_collision():
    for ball_b in BALLS:
        check1 = collide(MY_BALL,ball_b)
        if check1:
            a = MY_BALL.r
            b = ball_b.r
            if(a < b):
                    return False
            else:
                    ball_b.x = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.y = random.randint(int(-screen_width)+ max_ball_r,int(screen_width)-max_ball_r)
                    ball_b.goto(ball_b.x, ball_b.y)
                    ball_b.r = random.randint(min_ball_r,max_ball_r)
                    ball_b.color = (random.random(),random.random(),random.random())
                    dx = random.randint(min_ball_dx+6,max_ball_dx)
                    dy = random.randint(min_ball_dx+6,max_ball_dx)
                    while dx == 0 or dy == 0:
                        dx = random.randint(min_ball_dx+6,max_ball_dx)
                        dy = random.randint(min_ball_dx+6,max_ball_dx)
                    ball_b.dx = dx
                    ball_b.dy = dy
                    MY_BALL.r+=5
                    MY_BALL.shapesize(MY_BALL.r/10)
                    ball_b.shapesize(ball_b.r/10)
                    turtle.clear()
                    turtle.write("radius is: " + str(MY_BALL.r),move=False,align = "center",font=("Arial", 40, "normal"))
    return True

def Movearound(event):
    ##print(str(MY_BALL.x )+ "  " + str(MY_BALL.y))
    MY_BALL.goto(event.x-screen_width,-event.y+screen_height)
turtle.getcanvas().bind("<Motion>", Movearound)
turtle.listen()

##food = turtle.clone()
##food.penup()
##food.st()
##food.shape("triangle")
##food.color("yellow")
##id1 = []
##posx = []
##posxy = []
##def food1():
##   for i in range(number_of_balls):
##       x = random.randint(int(-screen_width),int(screen_width))
##       y = random.randint(int(-screen_height),int(screen_height))
##       food.goto(x,y)
##       id1.append(food.stamp())
##       posx[i] = food.xcor()
##       posy[i] = food.ycor()

       

while RUNNING:
    ##print("hi")
    if screen_width != turtle.getcanvas().winfo_width()/2 or screen_height != turtle.getcanvas().winfo_height()/2:
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_balls_collision()
    MY_BALL.move(screen_width,screen_height)
    RUNNING = check_myball_collision()
    MY_BALL.showturtle()
    turtle.update()
    time.sleep(sleep)
##    for i in range(len(id1)):
##        if posx[i] == MY_BALL.x and posy[i] == MY_BALL.y:
##           food.clearstamp(id1[i])
    ##turtle.penup()
    ##turtle.goto(250,-300)
    ##turtle.write("score is :" + str(MY_BALL.r)
    if MY_BALL.r >= 200:
        RUNNING = False
        turtle.clear()
        turtle.write("you won!!!",move=False,align = "center",font=("Arial", 100, "normal"))
        turtle.mainloop()
        print("You won the game!!!")
    elif RUNNING == False:
        turtle.clear()
        turtle.write("you lost!!!",move=False,align = "center",font=("Arial", 100, "normal"))
        turtle.mainloop()
    
