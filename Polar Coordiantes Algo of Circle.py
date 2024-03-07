import turtle
import math

# Function to draw a circle using polar coordinates
def draw_circle_polar(radius):
    turtle.speed(0)  # Set the drawing speed to the fastest
    turtle.penup()
    turtle.goto(radius, 0)  # Move turtle to the starting position
    turtle.pendown()

    for angle in range(361):  # Iterate through angles from 0 to 360 degrees
        x = radius * math.cos(math.radians(angle))  # Convert polar to Cartesian x-coordinate
        y = radius * math.sin(math.radians(angle))  # Convert polar to Cartesian y-coordinate
        turtle.goto(x, y)  # Move turtle to the new coordinates

    turtle.penup()
    turtle.hideturtle()
    turtle.done()

# Test the function with a radius of 100
draw_circle_polar(100)
