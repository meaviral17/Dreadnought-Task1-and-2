import turtle

smiley = turtle.Turtle()

smiley.speed(10)
smiley.pensize(2)

smiley.color("yellow")
smiley.begin_fill()
smiley.circle(100)
smiley.end_fill()

smiley.penup()
smiley.goto(-40, 50)
smiley.pendown()
smiley.color("black")
smiley.begin_fill()
smiley.circle(20)
smiley.end_fill()

smiley.penup()
smiley.goto(40, 50)
smiley.pendown()
smiley.begin_fill()
smiley.circle(20)
smiley.end_fill()

smiley.penup()
smiley.goto(-60, -30)
smiley.pendown()
smiley.color("black")
smiley.setheading(-60)
smiley.circle(80, 120)

smiley.hideturtle()

turtle.done()
