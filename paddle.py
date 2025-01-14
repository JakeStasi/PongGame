from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create(position)

    def create(self, position):
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        x = self.xcor()
        y = self.ycor() + 20
        self.goto(x, y)

    def down(self):
        x = self.xcor()
        y = self.ycor() - 20
        self.goto(x, y)
