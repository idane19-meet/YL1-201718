import turtle

turtle.ht()
turtle.tracer(1,0)
turtle.penup()
turtle.goto(-75,0)
turtle.pendown()
radius = 100
turtle.color("blue")
turtle.circle(radius)



turtle.penup()
turtle.goto(0,0)
turtle.color("black")
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(75,0)
turtle.color("red")
turtle.pendown()
turtle.circle(radius)


turtle.penup()
turtle.goto(-50,-100)
turtle.color("yellow")
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(50,-100)
turtle.color("green")
turtle.pendown()
turtle.circle(radius)

turtle.mainloop()
