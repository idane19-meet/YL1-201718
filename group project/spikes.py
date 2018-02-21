import turtle
import random
import math
turtle.setup(640,535)
import border
turtle.colormode(255)
turtle.tracer(1,0)
level = 0
spike = turtle.clone()
screen_height = turtle.window_height()-60
turtle.ht()
spike.penup()
spike.shape("triangle")
x_left = -290
x_right = 280
border_len = (int)(screen_height/2)
spike.shapesize(3)
##spike.degrees(-180)
edge = spike.clone()
edge.left(90)
start = -240
for i in range(11):
    edge.goto(start,-230)
    edge.stamp()
    start += 50

start = 240
edge.left(180)
for i in range(11):
    edge.goto(start,235)
    edge.stamp()
    start -= 50

spike.left(180)
color = random.randint(0,255),random.randint(0,255),random.randint(0,255)
def spikes():
    global level
    global color
    spike.color(color)
    num_of_spikes = random.randint(1,4)
    ##num_of_spikes = 4
    ypos = []
    ##print(num_of_spikes)
    for i in range(num_of_spikes):
        new_y = random.randint(-border_len, border_len)
        for current_y in ypos:
            while(current_y==new_y or abs(current_y-new_y)<= 30 or new_y < -210 or new_y > 206 or new_y > 230 or new_y < -230):
                new_y=random.randint(-border_len, border_len)
                ##print("sjkfhauks")
        ##print("Stamped at: "+str(new_y))
        ypos.append(new_y)
        if level%2 == 0:
            spike.goto(x_right,new_y)
            spike.stamp()
        else:
            spike.goto(x_right,new_y)                
            spike.stamp()
        level += 1
def write_level():
    global level
    global color
    turtle.ht()
    turtle.pensize(10)
    turtle.color(color)
    turtle.circle(60)
    turtle.penup()
    turtle.goto(0,30)
    turtle.write(level, True, align="center",font = ("Arial",50,"normal"))
write_level()
spikes()
