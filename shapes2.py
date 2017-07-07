from turtle import *
import math

# Name your Turtle.
tiny = Turtle()

# Set Up your screen and starting position.
tiny.penup()
setup(500,300)
x_pos = -250
y_pos = -150
tiny.setposition(x_pos, y_pos)

### Write your code below:
tiny.pendown()
tiny.speed(10)

colors = {"red","blue","pink","orange","teal","DarkCyan"}
for each_color in colors:
    angle = 360 / len(colors)
    tiny.color(each_color)
    tiny.circle(40)
    tiny.right(angle)
    tiny.forward(30)



# Close window on click.
exitonclick()
