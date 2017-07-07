from turtle import *
import math
import turtle
# The turtle is named after my tiny dog.
wn = turtle.Screen()
wn.bgcolor("lightgreen")
bam = Turtle()
bam.shape("turtle")
bam.color("grey")

# Set position
bam.penup()
setup(500,300)
x_pos = -250
y_pos = -150
bam.setposition(x_pos, y_pos)

### Code for shapes/colors
bam.pendown()
bam.pensize(5)

answer=input("Say a color...any color!")
bam.pencolor(answer)

def shape(steps, angle, speed1):
    bam.speed(speed1)
    bam.begin_fill()
    bam.fillcolor(answer)
    for shape in range(int(answer3)):
        bam.forward(steps)
        bam.left(angle)
    bam.end_fill()
answer2 = input("Enter an amount of steps:")
answer3 = input("Enter a side:")
answer4 = input("Enter a speed to travel:")
shape(int(answer2),360/int(answer3),int(answer4))

# Close window on click.
exitonclick()
