from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 8, "normal")

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.velo = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align= ALIGN, font= FONT)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.y_move += 0.5 if self.y_move > 0 else -0.5

        self.velo *= 0.9

    def ball_reset(self):
        self.goto(0,0)
        self.velo = 0.1
        self.bounce_x()



