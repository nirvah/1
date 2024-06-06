import turtle

# Set up the turtle screen 
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle instance 
t = turtle.Turtle()
t.speed(1)  # Set the drawing speed (1 is slow)
t.pensize(2)  # Set the pen size

# Define a function to draw a rectangle
def draw_rectangle(x, y, width, height, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Define a function to draw a circle
def draw_circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.circle(radius)

# Define a function to translate a 2D object
def translate(x, y, dx, dy):
    t.penup()
    t.goto(x + dx, y + dy)
    t.pendown()

# Define a function to rotate a 2D object
def rotate(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.left(angle)
    t.pendown()

# Draw a rectangle
draw_rectangle(-200, 0, 100, 50, "blue")

# Draw a translated rectangle
translate(-200, 0, 200, 0)
draw_rectangle(0, 0, 100, 50, "blue")

# Draw a rotated rectangle
rotate(0, 0, 45)
draw_rectangle(0, 0, 100, 50, "blue")

# Draw a circle
draw_circle(300, 0, 50, "red")

# Keep the window open until it's closed
turtle.done()
