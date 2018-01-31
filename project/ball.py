from turtle import Turtle

class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.shapesize(r/10)
        self.goto(x,y)
        self.shape("circle")
        self.dx = dx
        self.dy = dy
        self.r = r
        self.x = x
        self.y = y
        self.color(color)
    def move(self,screen_width,screen_height):
        current_x = self.xcor()
        new_x = current_x+self.dx
        current_y = self.ycor()
        new_y = current_y + self.dy
        right_side_ball = new_x + self.r
        up_side_ball = new_y + self.r
        left_side_ball = new_x -self.r
        down_side_ball = new_y - self.r
        self.goto(new_x,new_y)
        if((right_side_ball >= screen_width and self.dx > 0) or (left_side_ball <= -screen_width and self.dx < 0)):
            self.dx = -self.dx
            self.clear()
        elif((up_side_ball >= screen_height and self.dy > 0)or (down_side_ball <= -screen_height and self.dy< 0)):
           self.dy = -self.dy
           self.clear()
