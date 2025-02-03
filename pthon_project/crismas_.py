import turtle
import random
# Screen setup
screen = turtle.Screen()
screen.bgcolor("dark blue")
screen.title("Merry Christmas")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.color("green")

# Function to draw the tree
def draw_tree():
    pen.penup()
    pen.goto(0, -200)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("green")
    
    # Tree levels
    for level in range(3):
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
        pen.left(120)
        pen.forward(100)
        pen.left(120)
        pen.forward(50)
        pen.right(90)
        pen.forward(30)
        pen.left(90)
        pen.forward(50)
    pen.end_fill()

# Function to draw the trunk
def draw_trunk():
    pen.penup()
    pen.goto(-15, -200)
    pen.pendown()
    pen.begin_fill()
    pen.fillcolor("brown")
    for _ in range(2):
        pen.forward(30)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

# Function to add ornaments
def add_ornaments():
    pen.penup()
    pen.color("red")
    for _ in range(15):
        x = random.randint(-75, 75)
        y = random.randint(-180, 50)
        pen.goto(x, y)
        pen.dot(10)

# Function to write greeting
def write_greeting():
    pen.penup()
    pen.goto(0, 100)
    pen.color("white")
    pen.write("Merry Christmas!", align="center", font=("Arial", 24, "bold"))

# Draw the tree, trunk, and ornaments
draw_tree()
draw_trunk()
add_ornaments()

# Write the greeting
write_greeting()

# Hide the turtle
pen.hideturtle()

# Keep the screen open
turtle.done()
