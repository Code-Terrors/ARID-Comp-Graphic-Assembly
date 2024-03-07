import turtle

def draw_line_incremental(x1, y1, x2, y2):
    # Calculate the difference between endpoints
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps needed
    steps = max(abs(dx), abs(dy))

    # Calculate the increment in x and y for each step
    if steps != 0:
        x_increment = dx / steps
        y_increment = dy / steps
    else:
        x_increment, y_increment = 0, 0

    # Initialize the starting point
    x = x1
    y = y1

    # Move the turtle to the starting point
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    # Iterate over each step and draw the line
    for _ in range(steps):
        x += x_increment
        y += y_increment
        turtle.goto(round(x), round(y))

    # Draw the ending point
    turtle.goto(x2, y2)

# Set up the turtle
turtle.speed(0)  # Set the drawing speed to the fastest

# Test the function
x1, y1 = -100, -100
x2, y2 = 100, 100
draw_line_incremental(x1, y1, x2, y2)

# Keep the window open until it's closed by the user
turtle.done()
