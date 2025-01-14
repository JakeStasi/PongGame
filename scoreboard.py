from turtle import Turtle
#

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.hideturtle()
        self.update()


    def right_score(self):
        self.r_score += 1
        self.clear()
        self.update()

    def left_score(self):
        self.l_score += 1
        self.clear()
        self.update()

    def update(self):
        self.goto(300, 250)
        self.write(f"Score: {self.r_score}", move=True, align="right", font=("Arial", 15, "normal"))
        self.goto(-300, 250)
        self.write(f"Score: {self.l_score}", move=True, align="left", font=("Arial", 15, "normal"))

    def game_over(self,paddle_side):
        self.goto(0,0)
        self.write(f"Game Over! {paddle_side} side won ! ", align = "center",font=("Arial", 15, "normal") )
