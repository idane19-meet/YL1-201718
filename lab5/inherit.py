from turtle import *
import random
colormode(255)



class Square(Turtle):
    
    def __init__(self,size):
        Turtle.__init__(self)

        self.shapesize(size)
        self.shape("square")
    def random_color(self):
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        self.color(a,b,c)
                
        
shape1 = Square(3)
shape1.random_color()        
