import turtle
import winsound

class Ball():
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 1
        self.ball.dy = 1

    def get_x(self):
        return self.ball.xcor()

    def get_y(self):
        return self.ball.ycor()

    def goto(self):
        self.ball.goto(0,0)
        self.ball.dx = 1
        self.ball.dy = 1
        self.ball.dx *= -1

    def move_ball(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def onborder_collision(self):
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
            winsound.Beep(550, 50)

        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
            winsound.Beep(550, 50)

    def paddle_collision(self, paddle):
        if self.ball.xcor() > 340 and self.ball.xcor()<350 and self.ball.ycor() < (paddle.ycor() + 50) and self.ball.ycor() > (paddle.ycor() - 50):
            self.ball.setx(340)
            self.ball.dx *= -1.2
            winsound.Beep(550, 50)

        if self.ball.xcor() < -340 and self.ball.xcor()>-350 and self.ball.ycor() < (paddle.ycor() + 50) and self.ball.ycor() > (paddle.ycor() - 50):
            self.ball.setx(-340)
            self.ball.dx *= -1.2
            winsound.Beep(550, 50)

