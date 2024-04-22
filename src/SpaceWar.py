import os
import random
import turtle

turtle.Screen()
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)
turtle.mainloop()

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1


# Create Sprites
player = Sprite("triangle", "white", 0, 0)

while True: 
    player.fd(player.speed)
    