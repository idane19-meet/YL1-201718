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
##spike.pendown()
spike.left(180)
def spikes():
    global level
    spike.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    num_of_spikes = random.randint(1,5)
    num_of_spikes = 4
    ypos = []
    print(num_of_spikes)
    for i in range(num_of_spikes):
        new_y = random.randint(-border_len, border_len)
        for current_y in ypos:
            while(current_y==new_y or abs(current_y-new_y)<=30):
                new_y=random.randint(-border_len, border_len)
        print("Stamped at: "+str(new_y))
        ypos.append(new_y)
        if level%2 == 0:
            spike.goto(x_right,new_y)
            spike.stamp()
        else:
            spike.goto(x_right,new_y)                
            spike.stamp()
        level += 1
        
spikes()
