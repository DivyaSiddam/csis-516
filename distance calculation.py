

import turtle
# Test data sets
test_data = [
(50, 50, 25, 66, 55), # inside the circle
(50, 50, 100, 150, 150), # outside the circle
(50, 50, 100, 50, 150) # on the circle
]
# Iterate through each test case
for x1, y1, radius, x2, y2 in test_data:
# Calculate the distance between the point and the circle center
d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# Define tolerance for "on the circle"
tolerance = 1e-6
# Classify the point and set the color
if abs(d - radius) < tolerance:
color = "blue" # Point is on the circle
status = "The point is on the circle"
elif d < radius:
color = "green" # Point is inside the circle
status = "The point is inside the circle"
else:
color = "red" # Point is outside the circle
status = "The point is outside the circle"
# Draw the circle
turtle.penup() # Pull the pen up
turtle.goto(x1, y1 - radius) # Move to the starting position of the circle
turtle.pendown() # Pull the pen down to start drawing
turtle.circle(radius)
# Draw the point with the appropriate color
turtle.penup() # Pull the pen up
turtle.goto(x2, y2) # Move to the point position
turtle.pendown() # Pull the pen down to draw the point
turtle.dot(6, color) # Draw the dot with the color
# Draw the line connecting the circle center to the point
turtle.penup()
turtle.goto(x1, y1) # Move to the center of the circle
turtle.pendown()
turtle.goto(x2, y2) # Draw a line to the point
# Display the status near the circle
turtle.penup() # Pull the pen up
turtle.goto(x1 - 70, y1 - radius - 20) # Move to a position for the text
turtle.pendown() # Pull the pen down to write
turtle.write(status, font=("Times", 12))
# Hide the turtle before drawing the next case
turtle.hideturtle()
# Finish the turtle graphics and display the result
turtle.done()
