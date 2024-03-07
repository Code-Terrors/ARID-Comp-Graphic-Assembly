import turtle

# Create a turtle object
t = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)

# Define the radius of the circle
radius = 100

# Move the turtle to the starting position
t.penup()
t.goto(0, -radius)
t.pendown()

# Draw the circle using Cartesian coordinates
for _ in range(360):
    t.forward(2 * radius * 3.14159 / 360)  # Forward movement is proportional to the circumference formula
    t.left(1)  # Turn 1 degree left

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed by the user
screen.mainloop()
