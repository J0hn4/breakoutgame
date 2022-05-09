import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.shapesize(stretch_wid=2, stretch_len=5)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(position)
        self.showturtle()

    def remove(self):
        self.hideturtle()
        self.goto(700, 700)