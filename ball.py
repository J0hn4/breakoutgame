from turtle import Turtle
import random

X_RANDOM = random.randint(-3,3)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.goto(0,-200)
        self.showturtle()
        self.x_move = 0
        self.y_move = 0
        self.move_speed = 0.1

    def begin(self):
        self.y_move = 10
        self.x_move = X_RANDOM * 5
        while self.x_move == 0:
            self.x_move = X_RANDOM * 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_other_way(self):
        self.x_move *= -1

    def ball_reset(self):
        self.hideturtle()
        self.goto(0,-200)
        self.bounce_other_way()
        self.showturtle()

    def increase_speed(self):
        self.move_speed *= 0.5

    def ball_delete(self):
        self.hideturtle()