import turtle

class Paddle():
    def __init__(self, x):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(x, 0)
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)

    
    def ycor(self):
        return self.paddle.ycor()

    def xcor(self):
        return self.paddle.xcor()
    

    def move_paddle(self, key_press):
        if(key_press == "w" or key_press=="Up"):
            y = self.paddle.ycor()
            y += 20
            self.paddle.sety(y)
        elif(key_press == "s" or key_press=="Down"):
            y = self.paddle.ycor()
            y -= 20
            self.paddle.sety(y)

        