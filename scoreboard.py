from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-200, 250)

        self.update_score()

    def update_score(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def update_l(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over :(", align=ALIGNMENT, font=FONT)
