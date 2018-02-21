import turtle
import time
turtle.pendown()
bird=turtle.clone()
turtle.ht()

dy = 0.1
dx = 0.3
direction = "r"
SCREEN_WIDTH=turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT=turtle.getcanvas().winfo_height()/2

turtle.register_shape("birdRight.gif")
turtle.register_shape   ("birdLeft.gif")
bird.shape("birdRight.gif")
bird.penup()

SPACEBAR="space"
bird.st()
def move(screen_width,screen_height):
    global dx
    global direction
    current_x = bird.xcor()
    new_x=current_x+dx
    current_y=bird.ycor()
    new_y=current_y-dy
    bird.goto(new_x,new_y)
    if bird.xcor()>=screen_width or bird.xcor()<=-screen_width:
        dx = -dx
        if direction == "r":
            bird.shape("birdLeft.gif")
            direction = "l"
        else:
            bird.shape("birdRight.gif")
            direction = "r"

           
def jump():
    bird.penup()
    bird.goto(bird.xcor(),bird.ycor()+100)
turtle.onkeypress(jump, SPACEBAR)
turtle.listen()


        
    



