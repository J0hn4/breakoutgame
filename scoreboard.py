from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.write_new_score()
        # self.write_high_score()

    def write_new_score(self):
        self.clear()
        self.goto(0, -180)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 80, "normal"))

    def write_high_score(self):
        self.goto(0, 180)
        with open("highscore.txt") as data:
            self.high_score = int(data.read())
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.write(f"New High Score: {self.high_score}", align="center", font=("Courier", 80, "normal"))
        else:
            self.write(f"High Score: {self.high_score}", align="center", font=("Courier", 80, "normal"))

    def add_point(self):
        self.score += 1
        self.write_new_score()

    def print_game_over(self):
        self.clear()
        self.goto(0, 180)
        self.write(f"Game Over", align="center", font=("Courier", 80, "normal"))
        self.goto(0, -180)
        self.write(f"Final Score:{self.score}", align="center", font=("Courier", 80, "normal"))

