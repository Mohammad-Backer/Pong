from paddle import Paddle
from ball import Ball
import time
import turtle

def draw_window():
    wn= turtle.Screen()
    wn.title("Pong Game")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)
    return wn

def pen(score_a, score_b):
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courrier", 24, "normal"))
    return pen

def score(ball, score_b, score_a):
    if ball.get_x() < -390:
        ball.goto()
        score_b += 1
        return [score_a, score_b]

    if ball.get_x() > 390:
        ball.goto()
        score_a +=1
        return [score_a, score_b]

if __name__ == "__main__":
    wn = draw_window()
    ball = Ball()
    paddle_a = Paddle(-350)
    paddle_b = Paddle(350)
    score_a = 0
    score_b = 0
    pen = pen(score_a, score_b)
    wn.listen()
    wn.onkeypress(lambda : paddle_a.move_paddle('w'), "w")
    wn.onkeypress(lambda : paddle_a.move_paddle('s'), "s")
    wn.onkeypress(lambda : paddle_b.move_paddle('Up'), "Up")
    wn.onkeypress(lambda : paddle_b.move_paddle('Down'), "Down")

    scores = []
    while True:
        wn.update()
        ball.move_ball()
        ball.onborder_collision()
        ball.paddle_collision(paddle_a)
        ball.paddle_collision(paddle_b)
        scores = score(ball, score_b, score_a)
        try:
            score_a = scores[0]
            score_b = scores[1]
            pen.clear()
            pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courrier", 24, "normal"))
        except:
            pass
        scores = []        
        time.sleep(0.001)
