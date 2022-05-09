from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from brick import Brick
import time
from scoreboard import ScoreBoard
import random
import pygame

pygame.mixer.init()
death_sound = pygame.mixer.Sound("sfx_deathscream_robot2.wav")
bounce_sound = pygame.mixer.Sound("sfx_movement_jump2.wav")
game_over_sound = pygame.mixer.Sound("sfx_wpn_cannon2.wav")

# death_sound.play()
# ouch = pygame.mixer.Sound(os.path.join(s, 'ouch.ogg'))



screen = Screen()
screen.setup(width=1020, height=600)
screen.bgcolor("black")
screen.title("Breakout Game")
screen.tracer()

paddle = Paddle((0,-260))
ball =Ball()
scoreboard = ScoreBoard()
bricks = []
brick_number = 0
row_amount = 4

def create_field(rows=int):
    y_pos = 0
    for row in range(0, rows):
        x_pos = -440
        for brick in range(0,9):
            random_number = random.randint(-2, 4)
            brick_number = 1
            if random_number > 0:
                brick = Brick((x_pos, y_pos))
                bricks.append(brick)
            x_pos += 110
        y_pos += 50

def check_brick_collision():
    brick_amount = len(bricks)
    for brick in bricks:
        if ball.distance(brick) < 30:
            # ball.bounce()
            death_sound.play()
            brick.hideturtle()
            brick_amount -= 1
            # ball.bounce_other_way()
            x_axis_difference = ball.xcor() - brick.xcor()
            y_axis_difference = ball.ycor() - brick.ycor()
            if x_axis_difference - y_axis_difference >= 10:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                # ball.bounce()
                ball.bounce_other_way()
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                # ball.bounce()
                ball.bounce()
            bricks.remove(brick)
            scoreboard.add_point()
            # if scoreboard.score() % 8 == 0:
            #     ball.increase_speed()
            break
    if brick_amount == 0:
        row_amount = random.randint(3,6)
        create_field(rows=row_amount)

first_random_rows = random.randint(3,5)
create_field(rows=first_random_rows)

screen.listen()

screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(ball.begin,"space")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    if ball.xcor() > 500 or ball.xcor() < -500:
          ball.bounce_other_way()
          bounce_sound.play()

    if ball.ycor() > 300:
        ball.bounce()
        bounce_sound.play()

    if ball.distance(paddle) < 50 and ball.ycor() < -240:
        ball.bounce()
        bounce_sound.play()

    check_brick_collision()

    if ball.ycor() < -300:
         ball.ball_reset()
         game_is_on = False
         game_over_sound.play()
         # ball.increase_speed()

scoreboard.print_game_over()
ball.ball_delete()



screen.update()

screen.exitonclick()