import turtle

# Function to plot a point
def plot_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot()

# Function to draw the circle using Mid-Point Circle Drawing Algorithm
def mid_point_circle(radius):
    x = 0
    y = radius
    p = 1 - radius  # Initial value of the decision parameter

    plot_octant_points(x, y)  # Plot the initial octant points

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot_octant_points(x, y)  # Plot points in the current octant

# Function to plot points in one octant and use symmetry to plot points in the other seven octants
def plot_octant_points(x, y):
    plot_point(x, y)
    plot_point(y, x)
    plot_point(y, -x)
    plot_point(x, -y)
    plot_point(-x, -y)
    plot_point(-y, -x)
    plot_point(-y, x)
    plot_point(-x, y)

# Set up the turtle
turtle.speed(0)  # Set the drawing speed to the fastest

# Draw the circle with a radius of 100
mid_point_circle(100)

# Keep the window open until it's closed by the user
turtle.done()
