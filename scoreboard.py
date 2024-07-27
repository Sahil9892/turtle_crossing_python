from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.color("black")
        self.goto(-280, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align = ALIGNMENT, font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER!", align = "center" , font= FONT)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
    