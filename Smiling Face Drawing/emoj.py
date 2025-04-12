import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
my_turtle = turtle.Turtle()

# Draw the face
my_turtle.speed(10)
my_turtle.fillcolor("yellow")
my_turtle.begin_fill()
my_turtle.circle(100)
my_turtle.end_fill()

# Draw the left eye
my_turtle.penup()
my_turtle.goto(-35, 110)
my_turtle.pendown()
my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(15)
my_turtle.end_fill()

# Draw the right eye
my_turtle.penup()
my_turtle.goto(35, 110)
my_turtle.pendown()
my_turtle.fillcolor("black")
my_turtle.begin_fill()
my_turtle.circle(15)
my_turtle.end_fill()

# Draw the smile
my_turtle.penup()
my_turtle.goto(-42, 60)
my_turtle.setheading(-60)
my_turtle.pendown()
my_turtle.width(5)
my_turtle.circle(50, 125)

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()
