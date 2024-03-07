import turtle

def draw_line_bresenham(x1, y1, x2, y2):
    # Calculate the difference between endpoints
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Determine the direction of the line
    if x1 < x2:
        x_increment = 1
    else:
        x_increment = -1

    if y1 < y2:
        y_increment = 1
    else:
        y_increment = -1

    # Initialize the starting point
    x = x1
    y = y1

    # Move the turtle to the starting point
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Case where slope is less than 1
    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx):
            turtle.goto(x, y)
            if p >= 0:
                y += y_increment
                p -= 2 * dx
            x += x_increment
            p += 2 * dy

    # Case where slope is greater than or equal to 1
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            turtle.goto(x, y)
            if p >= 0:
                x += x_increment
                p -= 2 * dy
            y += y_increment
            p += 2 * dx

    # Draw the ending point
    turtle.goto(x2, y2)

# Set up the turtle
turtle.speed(0)  # Set the drawing speed to the fastest

# Test the function
x1, y1 = -100, -100
x2, y2 = 100, 100
draw_line_bresenham(x1, y1, x2, y2)

# Keep the window open until it's closed by the user
turtle.done()
