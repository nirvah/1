import turtle

def bresenham_line(x1, y1, x2, y2):
    dx, dy, sx, sy = abs(x2 - x1), abs(y2 - y1), (1 if x1 < x2 else -1), (1 if y1 < y2 else -1)
    err = dx - dy
    while True:
        turtle.goto(x1, y1)
        if x1 == x2 and y1 == y2: break
        if err * 2 > -dy: 
            err -= dy
            x1 += sx
        if err * 2 < dx:
             err += dx
             y1 += sy

turtle.speed(0)
turtle.penup()
turtle.goto(50, 100)
turtle.pendown()
bresenham_line(100, 120, 300, 200)
turtle.done()
